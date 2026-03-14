# Query Intent Agent

Purpose

Classify the retrieval need before any search begins.

## Inputs

- user task, question, or maintenance need
- repository ontology
- optional current project context

## Tasks

Determine:

- what kind of knowledge is being requested
- whether the query is:
  - active/current
  - durable/reference
  - operational/governance
  - historical
  - template/example
- likely note kind:
  - project artefact
  - area/governance note
  - topic note
  - atomic note
  - index
  - template
- likely PARA roots

Also rewrite vague queries into likely retrieval forms.

Example

Original query:

```text
what was that thing about not using document categories
```

Rewritten forms:

- avoid document-category folders
- classification by purpose not file type
- avoid bucket folders
- active outcome beats document type

## Output

```json
{
  "query_type": "",
  "time_orientation": "",
  "likely_note_kind": [],
  "likely_roots": [],
  "rewritten_queries": [],
  "confidence": ""
}
```

## Evaluation criteria

A good result:

- narrows the search space
- identifies the likely kind of knowledge
- generates useful rewritten forms
- avoids early overcommitment to one exact file

If uncertain:

- include multiple plausible roots or note kinds
- lower confidence rather than failing
