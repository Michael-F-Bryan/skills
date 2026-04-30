import argparse
import json
import re
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen

URL_PATTERN = re.compile(r"https?://[^\s\"'<>]+", re.IGNORECASE)
RELATIVE_SPEC_PATTERN = re.compile(
    r"(?P<quote>[\"'])"
    r"(?P<path>/[^\"']*(?:openapi|swagger|api-docs)[^\"']*)"
    r"(?P=quote)",
    re.IGNORECASE,
)

KNOWN_SPEC_URLS = (
    "https://api.clockify.me/api/v3/api-docs",
    "https://api.clockify.me/api/v1/api-docs",
    "https://docs.clockify.me/openapi.json",
    "https://docs.clockify.me/swagger.json",
)


def fetch_url(url: str, timeout: int = 30) -> bytes:
    request = Request(url, headers={"User-Agent": "clockify-openapi-downloader/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read()


def extract_candidate_urls(base_url: str, html: str) -> list[str]:
    candidates: list[str] = []
    seen: set[str] = set()

    for match in URL_PATTERN.findall(html):
        if any(token in match.lower() for token in ("openapi", "swagger", "api-docs")):
            if match not in seen:
                seen.add(match)
                candidates.append(match)

    for match in RELATIVE_SPEC_PATTERN.finditer(html):
        absolute = urljoin(base_url, match.group("path"))
        if absolute not in seen:
            seen.add(absolute)
            candidates.append(absolute)

    return candidates


def parse_openapi_document(payload: bytes) -> dict:
    document = json.loads(payload.decode("utf-8"))
    if not isinstance(document, dict):
        raise ValueError("Spec payload is not a JSON object.")
    if "paths" not in document:
        raise ValueError("Spec payload is missing required 'paths' field.")
    if "openapi" not in document and "swagger" not in document:
        raise ValueError("Spec payload is missing 'openapi' or 'swagger' version field.")
    return document


def download_openapi_spec(docs_url: str) -> tuple[dict, str]:
    docs_payload = fetch_url(docs_url)
    docs_html = docs_payload.decode("utf-8", errors="replace")
    candidates = extract_candidate_urls(docs_url, docs_html)

    for known_url in KNOWN_SPEC_URLS:
        if known_url not in candidates:
            candidates.append(known_url)

    attempts: list[str] = []
    for candidate_url in candidates:
        try:
            payload = fetch_url(candidate_url)
            document = parse_openapi_document(payload)
            return document, candidate_url
        except Exception as exc:  # noqa: BLE001
            attempts.append(f"{candidate_url}: {exc}")

    message = "Unable to locate a valid OpenAPI spec.\n" + "\n".join(attempts)
    raise RuntimeError(message)


def save_openapi_spec(document: dict, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    default_output = Path(__file__).resolve().parent.parent / "references" / "openapi.json"

    parser = argparse.ArgumentParser(description="Download Clockify OpenAPI spec from docs site.")
    parser.add_argument("--docs-url", default="https://docs.clockify.me/", help="Clockify docs URL")
    parser.add_argument(
        "--output",
        default=str(default_output),
        help="Output path for saved OpenAPI JSON",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    output_path = Path(args.output).expanduser().resolve()
    document, source_url = download_openapi_spec(args.docs_url)
    save_openapi_spec(document, output_path)
    print(f"Saved OpenAPI spec from {source_url} to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
