# Container Routing Agent

Purpose

Predict which containers are most likely to contain the answer.

## Inputs

```json
intent-report.json
```

and:

- repository tree
- container manifests
- optional `kb-index.json`

## Tasks

Rank candidate containers using:

- PARA root fit
- container name similarity
- manifest purpose match
- include/exclude rules
- known related containers
- current working context
- recency when relevant

The result should be a small ranked set of candidate containers.

Default target:

- 2 to 5 containers

Do not route to archives unless:

- the query is historical
- the active roots are exhausted
- a manifest or index explicitly points there

## Output

```json
{
  "candidate_containers": [
    {
      "path": "",
      "score": 0,
      "reasons": []
    }
  ],
  "fallback_containers": [],
  "confidence": ""
}
```

## Evaluation criteria

A good routing result:

- is small and plausible
- uses repository structure intelligently
- relies on manifests where available
- avoids sending the next step into broad scanning

If the repository lacks manifests:

- fall back to root + container names
- annotate the weaker basis for routing
