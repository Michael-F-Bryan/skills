# Labelling Sample: Dimension 14 - Concurrency Model Discipline

Dimension reminder: consistency and explicitness in concurrency primitives, ownership, cancellation, and lifecycle handling.

---

```rust
use std::sync::{Arc, Mutex};
use std::thread;

pub fn parallel_sum(values: Vec<u64>) -> u64 {
    let total = Arc::new(Mutex::new(0_u64));
    let mut handles = Vec::new();
    for chunk in values.chunks(4) {
        let local = chunk.to_vec();
        let total_ref = Arc::clone(&total);
        handles.push(thread::spawn(move || {
            let subtotal: u64 = local.iter().sum();
            let mut guard = total_ref.lock().unwrap();
            *guard += subtotal;
        }));
    }
    for h in handles {
        let _ = h.join();
    }
    *total.lock().unwrap()
}
```

- Score (1-5): 2
- Confidence (`low|medium|high`): medium
- Evidence:
  - I kinda got lost in the wall of code here
  - Normally I'd reach for something like `rayon` to do this for me rather than rolling my own thread pool
  - The size of the chunks is also a bit small, plus we're cloning them, so the performance overheads are going to outweigh any benefits we get from the parallelism

---

```go
package workers

import "context"

func Run(ctx context.Context, jobs <-chan string, handle func(context.Context, string) error) {
	for {
		select {
		case <-ctx.Done():
			return
		case job, ok := <-jobs:
			if !ok {
				return
			}
			_ = handle(ctx, job)
		}
	}
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): high
- Evidence:
  - Depending on the context, I'd probably write something like this for quick'n'dirty code... I have some concerns, though
  - There is no backpressure or concurrency limit, so we are opening ourselves up to spawning an unbounded number of goroutines
  - We should also decide how to handle the errors
  - 9 times out of 10, I'd probably reach for the `golang.org/x/sync/errgroup` package instead of writing this myself. It just gives you a cleaner way to deal with things like cancellation and errors and bounded concurrency

---

```python
import threading
import time

counter = 0


def worker() -> None:
    global counter
    for _ in range(1000):
        counter += 1
        time.sleep(0.0001)


def run() -> int:
    threads = [threading.Thread(target=worker) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return counter
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence:
  - I'm guessing this code is relying on the hopes and prayers, plus the GIL to avoid race conditions?

---

```ts
export async function processAll(ids: string[], runOne: (id: string) => Promise<void>): Promise<void> {
  const limit = 8;
  let i = 0;

  async function worker(): Promise<void> {
    while (true) {
      const index = i++;
      if (index >= ids.length) return;
      await runOne(ids[index]);
    }
  }

  await Promise.all(Array.from({ length: limit }, () => worker()));
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence:
  - This seems like a pretty good way to process all the items in parallel
