# Fallback Search Policy

Broad text search is a fallback, not the primary retrieval strategy.

## When to use fallback search

Use bounded text search only when:

- manifests do not resolve the query
- indexes do not surface likely candidates
- title and metadata shortlisting is weak
- the query is unusual or low-precision
- the repository lacks strong retrieval scaffolding

## Preferred fallback order

1. bounded search inside routed containers
2. bounded search across related containers
3. bounded archive search if historical
4. repo-wide search only as a last resort

## Search rules

Even when using grep-like tools:

- search rewritten queries, not just original wording
- search titles and metadata first where possible
- use multiple small searches rather than one broad dump
- do not open every hit deeply
- convert raw matches into a shortlist before reading

## Anti-pattern

Do not do this:

- grep the whole repo
- open dozens of hits
- read large bodies without routing or ranking

That is expensive, noisy, and error-prone.
