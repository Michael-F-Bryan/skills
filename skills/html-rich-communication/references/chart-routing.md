# Chart and Diagram Routing

Use this file when the artefact needs quantitative or relationship visualisation.

## Pick by communication job

| Job | Good defaults | Notes |
|---|---|---|
| Ranking | Ordered bar, lollipop, sorted card list | Position/length beats colour for comparison. |
| Exact comparison | Bar chart, table if few rows | Keep scales labelled and honest. |
| Change over time | Line, timeline, slope chart | Annotate the turning point or decision point. |
| Distribution | Histogram, box plot, density, dot plot | Good for analyst audiences; explain for lay readers. |
| Correlation | Scatterplot, quadrant plot | Warn against implied causality unless supported. |
| Part-to-whole | Stacked bar, treemap, simple percentage cards | Avoid pie/donut unless rough share is enough. |
| Spatial | Map, heatmap, route/coverage sketch | Use maps only when location is the point. |
| Process | Flowchart, swimlane, sequence diagram | Mermaid may be justified for complex flows. |
| State | State machine | Prefer explicit transitions and invalid states. |
| Architecture | Module map, layer cake, call flow | Anchor to file paths/services/contracts where possible. |
| Risk | Matrix, ranked risk cards, likelihood-impact map | Pair colour with text/icons. |
| Trade-off | 2x2 quadrant, option cards, spectrum | End with a recommendation or decision gate. |

## Perception rules

- Use position and length for quantitative comparison where possible.
- Use colour to reinforce meaning, not carry it alone.
- Avoid decorative area/volume encodings for precise comparison.
- Label axes and scales. If no scale exists, call the graphic conceptual.
- Annotate what the reader should notice.
- Keep mobile labels large enough to read.
