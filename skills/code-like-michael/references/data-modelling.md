# Data Modelling

Michael's approach to data modelling is built around a simple idea: **the shape of the code should help people do the right thing by default**.

That has two sides.

First, the model should make the system easier to *discover*. A good type carries meaning. It tells you what this thing is, what operations are valid, what data travels together, and what states or branches exist. That shows up in autocomplete, generated API docs, editor hints, compiler errors, and function signatures. When the model is good, a developer can often work productively just by following the types.

Second, the model should make the system harder to *misuse*. Invalid states should be excluded where practical. Operations should be available only when their preconditions are satisfied. The easiest code to write should also be the safest and most correct.

This is not "types for types' sake". It is about building APIs and domain models that are legible under tooling and resistant to accidental misuse.

## Types as executable documentation

A recurring theme in Michael's work is that types are not only for the compiler. They are a communication tool.

A function signature should tell you:

- what the caller must provide
- what guarantees the callee expects
- what comes back on success
- what kinds of failure matter

A domain type should tell you:

- what this value represents
- which fields belong together
- which combinations are meaningful
- which operations make sense on it

That improves day-to-day engineering in practical ways.

In an editor, stronger modelling gives you better autocomplete because the surface area is narrower and more semantically meaningful. Instead of digging through a generic object or bag of fields, the developer is guided toward the methods and properties that actually make sense.

In generated documentation or API schemas, well-shaped types make the system more legible. Consumers see domain concepts instead of loosely related primitives. A request type can express required versus optional fields, mutually exclusive branches, closed sets of variants, or lifecycle-specific payloads. That reduces the amount of tribal knowledge needed to use an API correctly.

## Correctness through construction

A stronger principle underneath is: construct valid things, not half-things.

Michael generally avoids APIs where you allocate an object and then separately "make it real" by calling methods like `initialize()`, `connect()`, `start()`, or `load()`. That style leaves too much room for misuse:

- callers can forget to call the second method
- methods can be called in the wrong order
- objects can exist in a limbo state where some operations are valid and some are not
- every consumer has to remember hidden lifecycle rules

Instead, he prefers construction paths that do the necessary setup up front and either:

- return a fully usable object, or
- fail immediately with an error that must be handled

That is essentially an RAII-style mindset applied broadly: if a value exists, it should already have acquired the resources or satisfied the invariants that define what it is.

## Make invalid states unrepresentable

A strong summary of the style is: use the model to rule out nonsense early.

That does not mean trying to encode every business rule in the type system at all costs. It means looking for places where the system can cheaply and clearly prevent bad states from existing in the first place.

Examples include:

- using distinct types for IDs that should not be confused
- using enums or tagged unions for closed sets of valid variants
- splitting one loose structure into several lifecycle-specific types
- hiding internal representation so callers cannot mutate fields arbitrarily
- requiring validated inputs before constructing core domain objects

Once bad states are excluded, downstream code becomes simpler because it no longer has to repeatedly defend against cases that were already ruled out.

## State-specific behaviour

A related pattern Michael uses a lot is a practical variant of the type state pattern.

The core principle is:

- encapsulate state internally
- expose only the operations that are valid in the current state
- require an explicit transition to get to a new state with a different valid surface area

In practice, that means avoiding "god objects" with methods that are technically callable at any time but only make sense in certain phases. Instead, each phase gets its own object or view of the object, with its own legal operations.

For example:

- an unvalidated config should not expose the same API as a validated runtime config
- a disconnected client should not expose the same operations as an authenticated session
- a draft command should not have the same methods as a submitted or persisted command
- a parsed-but-unresolved entity should not behave like a fully linked domain object

Sometimes that is implemented as separate concrete types. Sometimes it is hidden behind factory functions and narrow interfaces. The exact mechanism varies, but the design instinct is consistent.

## Encapsulation as modelling discipline

This style depends heavily on encapsulation.

If internal state is exposed too freely, the type system loses much of its power because callers can reassemble invalid combinations by hand. So Michael tends to keep representation details private and force interaction through deliberate constructors, factories, and methods that preserve invariants.

That is why he is often sceptical of data structures that are technically typed but semantically loose. A public struct with many mutable fields may satisfy the compiler while still leaving the domain model porous and easy to misuse. The important question is not just "is it typed?" but "does the type actually protect the concept it claims to represent?"

## Discovery and correctness reinforce each other

One of the stronger aspects of this approach is that the "developer experience" side and the "correctness" side are not separate concerns. They support each other.

When the model is precise:

- autocomplete becomes more useful because fewer irrelevant operations are visible
- docs become clearer because the domain concepts are explicit
- compiler errors become more informative because the mismatch is semantic, not incidental
- refactoring becomes safer because invariants are concentrated in constructors and type boundaries
- the happy path becomes easier to follow because it is encoded in the API surface

That is why strong data modelling is worth the effort even outside traditionally "type-heavy" languages. You are not just satisfying a compiler. You are building an interface that teaches people how to use the system.

## Practical rather than dogmatic

There is an important qualifier: this is not maximalist type-level programming for its own sake.

Michael's style is pragmatic. He uses the type system where it buys real leverage:

- better discovery
- fewer invalid states
- clearer lifecycles
- simpler downstream code
- more trustworthy boundaries

He is not trying to force every transient detail into an elaborate compile-time proof. The goal is to encode the important invariants at the level where doing so meaningfully improves the system.

That usually leads to designs that feel straightforward rather than fancy:

- factory functions instead of multi-step initialisation
- validated types instead of repeated runtime checks
- separate state-specific objects instead of one object with hidden lifecycle traps
- narrow method sets instead of broad, conditionally valid APIs

A good modelling choice should generally pay for itself in one or more of these ways:

- clearer editor guidance
- clearer signatures and docs
- fewer runtime checks scattered through the code
- fewer impossible branches
- less defensive programming in downstream logic

If it does not buy one of those things, it may be too clever.

## Rules of thumb

When revising code to match Michael's style:

- Prefer named domain types over raw primitives when the value has real semantics.
- Prefer enums, tagged unions, and explicit variants over stringly-typed mode fields.
- Prefer constructors and factory functions that return fully usable objects or fail immediately.
- Avoid `initialize()`, `connect()`, `load()`, or `start()` methods on otherwise incomplete objects unless the lifecycle is genuinely external and cannot be made safer.
- Prefer lifecycle-specific types or objects when different phases allow different operations.
- Keep internal representation private when exposing it would let callers bypass invariants.
- Use the type system to improve autocomplete, editor guidance, and generated docs, not just correctness.
- Do not collapse multiple distinct workflows into one "options bag" API just to save a few type definitions.
- Do not introduce wrapper types mechanically. Introduce them when they remove ambiguity, encode validation, or make downstream code materially clearer.
- In dynamic languages, apply the same principles with validation, frozen data structures, factory functions, and narrower public APIs.

## Summary

Michael's data modelling style treats types as part of the architecture, not just part of the syntax.

He uses them to improve discovery by making APIs legible to humans and tools, and to improve correctness by preventing invalid states and invalid operations from being easy to express. He prefers construction paths that return fully valid objects or fail immediately, rather than half-initialised objects with hidden lifecycle rules. He often applies type-state principles, formally or informally, so each state exposes only the operations that make sense for that state.

The overall effect is code that is easier to navigate, harder to misuse, and more honest about what is actually true at any given point in the system.

---

# Write this, not that

## Closed sets: model explicitly, not as strings

Instead of using a stringly-typed mode field and relying on comments or docs to explain valid values:

**Not this:**

```ts
type CrawlJob = {
  url: string;
  mode: string; // "snapshot", "interactive", or "deep"
};
```

**Write this:**

```ts
type CrawlMode = "snapshot" | "interactive" | "deep";

interface CrawlJob {
  url: string;
  mode: CrawlMode;
}
```

**Why:** Better autocomplete, better generated docs, better narrowing, and fewer "this should never happen" branches downstream.

## Variants with different data: use tagged unions

When variants actually carry different data, encode that directly instead of smearing everything into one shape.

**Not this:** A single object with several optional fields and some implicit rule saying "these three fields must appear together".

**Write this:**

```ts
type AuthConfig =
  | { kind: "apiKey"; apiKey: string }
  | { kind: "oauth"; clientId: string; clientSecret: string; tokenUrl: string };
```

**Why:** Much more useful in editors, reviews, and API docs. Tools can understand and narrow on `kind`.

## Construction: return a connected resource, not a "maybe ready" object (Go)

**Not this:** Split creation from readiness; leave a Client in an invalid or incomplete state.

```go
func NewClient(baseURL string) *Client {
	return &Client{
		baseURL: baseURL,
		http:    &http.Client{Timeout: 10 * time.Second},
	}
}

func (c *Client) Authenticate(ctx context.Context, clientID, clientSecret string) error {
	// ... c.token = "..."
	return nil
}
```

**Write this:** A constructor or factory that returns a fully usable value.

```go
func NewAuthenticatedClient(
	ctx context.Context,
	baseURL string,
	httpClient *http.Client,
	clientID string,
	clientSecret string,
) (*Client, error) {
	if httpClient == nil {
		httpClient = &http.Client{Timeout: 10 * time.Second}
	}
	// exchange credentials...
	token := "..."
	return &Client{
		baseURL: baseURL,
		token:   token,
		http:    httpClient,
	}, nil
}
```

**Why:** Callers get either a ready-to-use authenticated client or an error they must handle. The invalid intermediate state no longer exists as part of normal usage.

## Construction: return a usable object immediately (Python)

**Not this:** Objects that require a second lifecycle step before they are safe to use.

```python
class S3Bucket:
    def __init__(self, name: str) -> None:
        self.name = name
        self._client = None

    def connect(self) -> None:
        self._client = boto3.client("s3")

    def put_json(self, key: str, payload: dict[str, object]) -> None:
        assert self._client is not None
        self._client.put_object(...)
```

**Write this:** Construction that returns a usable object immediately.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class S3Bucket:
    name: str
    client: S3Client

    def put_json(self, key: str, payload: dict[str, object]) -> None:
        self.client.put_object(
            Bucket=self.name,
            Key=key,
            Body=json.dumps(payload).encode("utf-8"),
            ContentType="application/json",
        )

def connect_bucket(name: str, session: boto3.session.Session) -> S3Bucket:
    client = session.client("s3")
    return S3Bucket(name=name, client=client)
```

**Why:** If setup can fail, it fails before the object exists in the caller's hands. No assert on `_client`; the type is always valid.

## Validated domain types instead of raw primitives (Rust)

**Not this:** Broad structs full of primitive fields that only become meaningful through convention.

```rust
pub struct DeploymentRequest {
    pub service: String,
    pub environment: String,
    pub replicas: u32,
}
```

**Write this:** Domain types with validation at the boundary.

```rust
#[derive(Debug, Clone)]
pub struct ServiceName(String);

impl ServiceName {
    pub fn parse(s: impl Into<String>) -> Result<Self, ServiceNameError> {
        let s = s.into();
        if s.is_empty() {
            return Err(ServiceNameError::Empty);
        }
        // ... validate ...
        Ok(Self(s))
    }
    pub fn as_str(&self) -> &str {
        &self.0
    }
}

#[derive(Debug, Clone, Copy)]
pub enum Environment {
    Dev,
    Staging,
    Prod,
}

#[derive(Debug, Clone, Copy)]
pub struct ReplicaCount(u16);

impl ReplicaCount {
    pub fn new(value: u16) -> Result<Self, ReplicaCountError> {
        if value == 0 {
            return Err(ReplicaCountError::ZeroNotAllowed);
        }
        Ok(Self(value))
    }
}

pub struct DeploymentRequest {
    pub service: ServiceName,
    pub environment: Environment,
    pub replicas: ReplicaCount,
}
```

**Why:** Confusing values produce real bugs. Validated types improve the rest of the API surface. A good litmus test: would a raw String or u32 force every caller to remember hidden rules? If yes, the model is too weak.

## State-specific API: give each lifecycle phase its own surface area (TypeScript)

**Not this:** One class that exists in multiple modes and forces every method to defend itself at runtime.

```ts
class UploadSession {
  private token?: string;

  async authenticate(): Promise<void> {
    this.token = await fetchToken();
  }

  async upload(file: File): Promise<void> {
    if (!this.token) throw new Error("not authenticated");
    // ...
  }

  async complete(): Promise<void> {
    if (!this.token) throw new Error("not authenticated");
    // ...
  }
}
```

**Write this:** Explicit phases with different types.

```ts
class PendingUploadSession {
  constructor(private readonly baseUrl: string) {}

  async authenticate(credentials: Credentials): Promise<AuthenticatedUploadSession> {
    const token = await fetchToken(this.baseUrl, credentials);
    return new AuthenticatedUploadSession(this.baseUrl, token);
  }
}

class AuthenticatedUploadSession {
  constructor(
    private readonly baseUrl: string,
    private readonly token: string,
  ) {}

  async upload(file: File): Promise<void> {
    // token is guaranteed to exist here
  }

  async complete(): Promise<void> {
    // token is guaranteed to exist here
  }
}
```

**Why:** The method set itself teaches the lifecycle: pending sessions can authenticate; authenticated sessions can upload and complete. Autocomplete becomes a guide to valid behaviour.

## State-specific types (Rust)

**Not this:** One type with both parse and deploy and implicit state.

**Write this:**

```rust
pub struct ParsedManifest {
    raw: serde_json::Value,
}

pub struct ValidatedManifest {
    name: ServiceName,
    image: ImageRef,
    replicas: ReplicaCount,
}

impl ParsedManifest {
    pub fn validate(self) -> Result<ValidatedManifest, ManifestError> {
        // ...
    }
}

impl ValidatedManifest {
    pub fn deploy(&self, client: &DeployClient) -> Result<DeploymentId, DeployError> {
        // ...
    }
}
```

**Why:** Invalid operations are made awkward or impossible. You cannot call `deploy` on unvalidated data.

## Encapsulation: expose behaviours that preserve invariants (Python)

**Not this:** Mutable bags that expect every caller to remember the rules.

```python
@dataclass
class RetryPolicy:
    max_attempts: int
    backoff_seconds: float
    jitter: bool
```

**Write this:** Validation and controlled construction.

```python
@dataclass(frozen=True)
class RetryPolicy:
    max_attempts: int
    backoff_seconds: float
    jitter: bool

    @classmethod
    def create(cls, max_attempts: int, backoff_seconds: float, jitter: bool) -> "RetryPolicy":
        if max_attempts < 1:
            raise ValueError("max_attempts must be >= 1")
        if backoff_seconds < 0:
            raise ValueError("backoff_seconds must be >= 0")
        return cls(
            max_attempts=max_attempts,
            backoff_seconds=backoff_seconds,
            jitter=jitter,
        )
```

**Why:** Even in a dynamic language, the construction path carries correctness. Nonsensical values like `max_attempts=0` or negative backoff cannot be constructed through the public API.

## API shape: so tools can teach the user (Go)

**Not this:** A generic function with a loose bag of configuration and undocumented constraints.

```go
type RunOptions struct {
	Mode        string
	OutputPath  string
	Verbose     bool
	Checkpoint  *string
	ResumeFrom  *string
}

func Run(ctx context.Context, opts RunOptions) error {
	// ...
}
```

**Write this:** Explicit branches with distinct types and functions.

```go
type SnapshotRun struct {
	OutputPath string
	Verbose    bool
}

type ResumeRun struct {
	OutputPath string
	Verbose    bool
	Checkpoint string
}

func RunSnapshot(ctx context.Context, run SnapshotRun) error {
	// ...
}

func ResumeFromCheckpoint(ctx context.Context, run ResumeRun) error {
	// ...
}
```

**Why:** The API becomes self-describing in editor hints and generated docs. Callers are much less likely to put together nonsense combinations. Yes, this creates more named types and functions—that is often a good trade when the alternative is one over-generalised entrypoint with hidden rules.
