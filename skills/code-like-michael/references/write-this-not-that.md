# Write This, Not That

Use these examples to turn the fingerprint into concrete code choices.

## Composition Root

Write this:

```go
func run(ctx context.Context, cfg Config) error {
	client, err := newClient(cfg)
	if err != nil {
		return fmt.Errorf("create client: %w", err)
	}

	doc, err := fetchDocument(ctx, client, cfg.DocumentURL)
	if err != nil {
		return fmt.Errorf("fetch document: %w", err)
	}

	outcome := validateDocument(doc)
	return renderOutcome(outcome)
}
```

Not this:

```go
func Run(ctx context.Context, cfg Config) error {
	return NewApplication(
		NewRuntime(
			NewDocumentService(
				NewValidationManager(),
			),
		),
	).Execute(ctx, cfg)
}
```

Why:
- keep execution order recoverable from one place
- wire dependencies visibly
- do not hide simple orchestration behind speculative object graphs

## Naming

Write this:
- `ValidationOutcome`
- `RequestID`
- `LinkDiagnostics`
- `FetchDocument()`
- `parseConfig()`

Not this:
- `Processor`
- `Manager`
- `CommonData`
- `HandleThing()`
- `Utils`

Why:
- names should reveal domain meaning or stage in the flow
- generic nouns hide ownership and policy

## Boundary Wrappers

Write this:

```rust
pub struct HashedRegex(String, Regex);

impl HashedRegex {
    pub fn new(pattern: &str) -> Result<Self, regex::Error> {
        Ok(Self(pattern.to_owned(), Regex::new(pattern)?))
    }
}
```

Not this:

```rust
pub type Pattern = Regex;
```

Why:
- add a wrapper when local semantics matter, such as hashing, serialisation, or policy
- do not wrap a tool unless the wrapper adds meaning

## Framework Boundaries

Write this:

```go
func (h *Handler) GetDocument(w http.ResponseWriter, r *http.Request) {
	req, err := decodeGetDocumentRequest(r)
	if err != nil {
		writeError(w, errcode.InvalidArgument, err)
		return
	}

	outcome, err := h.service.GetDocument(r.Context(), req)
	if err != nil {
		writeServiceError(w, err)
		return
	}

	writeJSON(w, http.StatusOK, outcome)
}
```

Not this:

```go
func (h *Handler) GetDocument(w http.ResponseWriter, r *http.Request) {
	outcome, err := h.service.GetDocument(r.Context(), r)
	if err != nil {
		http.Error(w, err.Error(), 500)
		return
	}

	json.NewEncoder(w).Encode(outcome)
}
```

Why:
- transport types may appear at the boundary
- local semantics should start with explicit decoding and mapping
- do not let `*http.Request` become your domain model

## Validation Placement

Write this for integrity boundaries:

```go
func decodeGetDocumentRequest(r *http.Request) (GetDocumentRequest, error) {
	var req GetDocumentRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		return GetDocumentRequest{}, fmt.Errorf("decode request: %w", err)
	}
	if req.URL == "" {
		return GetDocumentRequest{}, errors.New("missing url")
	}
	return req, nil
}
```

Not this:

```go
func (s *Service) GetDocument(ctx context.Context, req GetDocumentRequest) (Outcome, error) {
	if req.URL == "" {
		return Outcome{}, errors.New("missing url")
	}
	// more business logic...
}
```

Why:
- config, auth, IDs, and request shape should usually fail at ingress

Write this for diagnostic-heavy flows:

```rust
pub fn parse(input: &str) -> ParseResult {
    let mut diagnostics = Vec::new();
    let syntax = parse_lossy(input, &mut diagnostics);
    ParseResult { syntax, diagnostics }
}
```

Not this:

```rust
pub fn parse(input: &str) -> Result<SyntaxTree, Error> {
    parse_strict(input)
}
```

Why:
- if diagnostics are the product, preserve enough structure to report more than one failure

## Abstraction Threshold

Write this:

```go
func decodeCreateUserRequest(r *http.Request) (CreateUserRequest, error) { ... }
func decodeUpdateUserRequest(r *http.Request) (UpdateUserRequest, error) { ... }
```

Not this:

```go
func decodeRequest[T any](r *http.Request) (T, error) { ... }
```

Why:
- keep semantically different mappings separate until the shared policy is truly stable

Write this when repetition is genuinely mechanical:

```go
//go:generate go run ./cmd/genschema
```

Not this:

```go
// copied generated shape by hand in three packages
```

Why:
- mechanical repetition should be generated or checked, not manually mirrored

## Error Handling

Write this:

```go
doc, err := repo.Load(ctx, id)
if err != nil {
	return fmt.Errorf("load document %q: %w", id, err)
}
```

Not this:

```go
doc, err := repo.Load(ctx, id)
if err != nil {
	return err
}
```

Why:
- wrap at meaningful boundaries with stable context

Write this:

```rust
assert!(generated == checked_in, "generated file is stale");
```

Not this:

```rust
return Err(anyhow!("generated file is stale"));
```

Why:
- stale generated artefacts are often invariant failures in developer workflows, not runtime business errors

## Tests

Write this:

```go
func TestGetDocument_RejectsMissingURL(t *testing.T) { ... }
func TestGetDocument_ReturnsMixedDiagnostics(t *testing.T) { ... }
func TestGeneratedOpenAPIIsUpToDate(t *testing.T) { ... }
```

Not this:

```go
func TestHandler_CallsServiceWithExpectedArguments(t *testing.T) { ... }
```

Why:
- prefer tests that prove request paths, behaviour, fixtures, and drift surfaces
- do not couple tests to private choreography when public behaviour is cheap to exercise

## Comments

Write this:

```go
// Reject missing project IDs here so downstream code can assume ownership is known.
```

Not this:

```go
// Check if project ID is empty.
```

Why:
- explain intent, invariants, or trade-offs
- do not narrate the obvious

## Generated And Derived Artefacts

Write this:
- check in generated output when the repo expects it
- add a test or command that fails on drift
- keep the human-owned source of truth small

Not this:
- manually edit generated files
- rely on contributors to remember regeneration by habit
- keep codegen hidden with no verification

## Fast Smell Test

The result is probably off-style if it contains:
- `utils`, `common`, `base`, or `manager` as a new home for unrelated logic
- a generic repository/service layer added before there is repeated policy to justify it
- request or config validation pushed deep into domain code
- mock-heavy tests around an interface invented only for the test
- wrappers around `chi`, `gqlgen`, `sqlc`, `bob`, OpenAPI tools, or Terraform that add no local semantics
