# Design decisions, risks, and metric provenance

## Design decision pattern

Use this instead of “why it is built this way”.

```markdown
### Decision: <plain name>

- Selected direction:
- Why:
- Alternatives considered:
- What this buys us:
- Accepted risk / trade-off:
- Validation state:
- Revisit trigger:
```

A good decision section gives reviewers a surface for disagreement.

## Metric provenance

Prominent numbers must declare:

| Field | Meaning |
|---|---|
| Number | The value as displayed |
| Type | measured / code default / config default / inferred / requirement / target / forecast / assumption / promise |
| Source | File, log, person, system, or calculation |
| Validation state | validated / partially validated / unvalidated / stale / unknown |
| Implication | What decision or risk depends on it |
| Visual treatment | how confidently it may be displayed |

Unvalidated defaults should not be styled like measured facts.

## Risk shape

For meaningful risks:

- risk;
- impact;
- likelihood or confidence;
- mitigation;
- owner;
- review/revisit trigger.
