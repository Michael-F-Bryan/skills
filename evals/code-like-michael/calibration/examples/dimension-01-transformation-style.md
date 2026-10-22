# Labelling Sample: Dimension 1 - Transformation Style

Dimension reminder: preference for declarative transformation pipelines/combinators vs imperative mutation loops for transform-heavy logic.

---

```rust
pub fn normalize_usernames(raw: &[String]) -> Vec<String> {
    raw.iter()
        .map(|s| s.trim().to_lowercase())
        .filter(|s| !s.is_empty())
        .map(|s| s.replace(' ', "_"))
        .collect()
}
```

- Score (1-5): 5
- Confidence (`low|medium|high`): high
- Evidence: The function is a simple transformation of a list of strings, with no complex logic or branching. It is quite clear that we're making sure each username is lowercase, filtering out empty ones, and replacing spaces with underscores.

---

```rust
pub fn active_ids(users: &[User]) -> Vec<u64> {
    let mut out = Vec::new();
    for user in users {
        if user.is_active {
            out.push(user.id);
        }
    }
    out
}

pub struct User {
    pub id: u64,
    pub is_active: bool,
}
```

- Score (1-5): 1
- Confidence (`low|medium|high`): high
- Evidence: Why didn't you just write a `map()`?

---

```rust
pub fn cleaned_prices(values: &[f64]) -> Vec<i64> {
    let mut normalised = Vec::new();

    for value in values {
        if value.is_finite() {
            normalised.push((value * 100.0).round() as i64);
        }
    }

    normalised.sort_unstable();
    normalised.dedup();
    normalised
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence: I would have preferred to use a `map()` here instead of the loop. The sort and dedup are pragmatic and I would leave them be.

---

```rust
pub fn top_tags(lines: &[String]) -> Vec<(String, usize)> {
    let mut counts = std::collections::HashMap::<String, usize>::new();

    for line in lines {
        for token in line.split(',') {
            let tag = token.trim().to_lowercase();
            if tag.is_empty() {
                continue;
            }
            let next = counts.get(&tag).copied().unwrap_or(0) + 1;
            counts.insert(tag, next);
        }
    }

    let mut pairs: Vec<(String, usize)> = counts.into_iter().collect();
    pairs.sort_by(|a, b| b.1.cmp(&a.1).then_with(|| a.0.cmp(&b.0)));
    pairs.into_iter().take(5).collect()
}
```

- Score (1-5): 3
- Confidence (`low|medium|high`): medium
- Evidence: The code is okay, but it took me a non-trivial amount of time to understand what it was doing. I would probably write it as...

```rust
use std::collections::BTreeMap;

pub fn top_tags(lines: &[String]) -> Vec<(String, usize)> {
    let tags = lines
        .iter()
        .flat_map(|line| line.split(','))
        .map(str::trim)
        .filter(|tag| !tag.is_empty())
        .map(str::to_lowercase);

    let mut counts = BTreeMap::new();

    for tag in tags {
        *counts.entry(tag).or_insert(0) += 1;
    }

    let mut pairs: Vec<_> = counts.into_iter().collect();

    pairs.sort_by(compare_tag_counts);

    pairs.truncate(5);
    pairs
}

fn compare_tag_counts(a: &(String, usize), b: &(String, usize)) -> std::cmp::Ordering {
    let (tag_a, count_a) = a;
    let (tag_b, count_b) = b;

    count_b
        .cmp(count_a)        // highest count first
        .then_with(|| tag_a.cmp(tag_b)) // alphabetical tie-break
}
```
