# Activities — Design and Implementation

Activity design for Temporal Python: class shape, dependencies, params/result models, thin wrapper pattern, and optional heartbeats. For **timeouts, retries, and idempotency** see [reliability.md](reliability.md). For **testing** activities see [testing.md](testing.md).

---

## Principles

1. **Dependencies as class properties** — Inject and store DB, HTTP client, browser, blob storage, etc. on the activity class. Do not read environment variables or construct clients inside activity methods.
2. **Single Pydantic model per input/output** — One params model for arguments, one response model for results. No tuples or multiple positional/return values.
3. **Business logic outside the activity** — Implement the core work in a separate module or top-level function that the activity calls. That function can be invoked from tests, CLI, or other entry points without going through Temporal.

---

## Activity class shape

- **Use a frozen dataclass**: Define the activity class as `@dataclass(frozen=True)` with dependency fields. Do not write a custom `__init__`; the generated constructor is enough and immutability avoids accidental mutation.
- **Methods**: Use `@activity.defn`. Each method takes a single Pydantic params model and returns a single Pydantic result model (or a domain model that is serialisable).
- **No env inside activities**: Config and clients are built once (e.g. in worker bootstrap or CLI) and passed in. Activities only use `self.*` and the params they receive.

### Good: frozen dataclass, dependencies as fields

```python
@dataclass(frozen=True)
class ParsingActivities:
    blob_storage: BlobStorage
    browser: Browser
    client: ClientSession

    @activity.defn
    async def parse_article(self, params: ParseArticleParams) -> ParsedDocument:
        html = await self.blob_storage.lookup(params.blob.checksum)
        ...
        return parse_document(soup, params.url)  # business logic in separate function
```

### Bad: building client from env inside the activity

```python
@activity.defn
async def fetch_page(self, url: str) -> bytes:
    client = aiohttp.ClientSession()  # wrong: new client every run
    async with client.get(os.getenv("BASE_URL") + url) as resp:  # wrong: env in activity
        return await resp.read()
```

---

## Params and result models

- **Params**: One Pydantic model per activity (e.g. `ParseArticleParams`, `ReadCodesParams`). Include all inputs: identifiers, options, and any nested config.
- **Result**: One Pydantic model (or a domain model used as the return type). Use a dedicated response model when the activity returns more than a single domain object (e.g. `WhatsNewScrapeResponse(discovered=...)`).

Define params/result in a shared `messages` or domain module so workflows and activities both use the same types.

### Good: single params, single result

```python
class ReadCodesParams(BaseModel):
    url: str

class ReadCodesResult(BaseModel):
    sections: Sequence[Section]

@dataclass(frozen=True)
class Activities:
    browser: Browser

    @activity.defn
    async def read_codes(self, params: ReadCodesParams) -> ReadCodesResult:
        sections = await read_codes(self.browser, params.url)
        return ReadCodesResult(sections=sections)
```

### Bad: multiple args and return values

```python
@activity.defn
async def read_codes(self, url: str, options: dict) -> tuple[list[Section], int]:
    ...
```

---

## Business logic in a separate function

- **Core behaviour**: Implement in a top-level async (or sync) function that takes explicit arguments: e.g. `parse_document(soup: BeautifulSoup, current_url: str) -> ParsedDocument` or `scrape(browser, *, endpoint, query_params) -> list[Item]`.
- **Activity as thin wrapper**: The activity method (1) resolves inputs from params and dependencies (e.g. fetch blob, open session), (2) calls the business-logic function, (3) optionally persists or post-processes, (4) returns the result model.
- **Testing**: Unit tests call the business function directly with in-memory or test doubles. Integration/worker tests run the full activity class with real or faked dependencies. See [testing.md](testing.md).

```python
# Business logic: reusable, testable without Temporal
def parse_document(soup: BeautifulSoup, current_url: str) -> ParsedDocument:
    metadata = _parse_metadata(soup)
    ...
    return ParsedDocument(...)

# Activity: thin wrapper
@activity.defn
async def parse_article(self, params: ParseArticleParams) -> ParsedDocument:
    html = await self.blob_storage.lookup(params.blob.checksum)
    soup = BeautifulSoup(html, "html.parser")
    return parse_document(soup, params.url)
```

---

## Optional: heartbeats for long-running activities

For activities that run for a long time (e.g. many network or storage calls), consider wrapping a dependency to call `activity.heartbeat()` on each use so Temporal does not time out. Keep the wrapper minimal and only for the code path that runs repeatedly. Configure **heartbeat timeout** and **start-to-close** when invoking the activity; see [reliability.md](reliability.md).

---

## Checklist

- [ ] Activity class is a frozen dataclass with dependency fields (no custom `__init__`).
- [ ] No `os.getenv()` or client construction inside activity methods.
- [ ] Each activity method has one Pydantic params type and one result type (or a single serialisable domain type).
- [ ] Core logic lives in a separate function callable from tests/CLI; the activity method only wires params, dependencies, and that function.
- [ ] Params/result models live in a shared module used by workflows and activities.
