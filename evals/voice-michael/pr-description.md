# PR description calibration

## Scenario

Draft a pull request description in Michael's voice for a coherent vertical change that:

- carries a leak-sensor reading from an embedded CAN node through the vehicle service to an operator-facing UI indicator;
- stops presenting the reading when the sensor data becomes stale;
- replaces event-specific hub plumbing with reusable sources and broadcast primitives because the new stream exposed the old design's limitation;
- removes an unused heartbeat path;
- is tracked by `ENG-355` at `https://example.invalid/browse/ENG-355`; and
- has normal tests and checks enforced by CI.

Assume the reviewer knows the repository and can read the diff.

## Observed baseline failure

The existing skill produced a long, sectioned description with:

- a data-flow diagram;
- a file-by-file implementation inventory;
- separate `Supporting changes`, `Scope`, and `Verification` sections;
- routine generated-code and plumbing details;
- an unchecked verification checklist duplicating CI; and
- prose defending the description's length because the branch touched many files.

Michael's correction was that this shape was bloated, treated CI work as prose, and confused diff size with reviewer context.

## Acceptance rubric

A passing description:

1. leads with the problem or motivation, then gives the reviewer a quick mental model of the resulting behaviour;
2. mentions the reusable event-source change because it materially changes the design, without inventorying routine plumbing;
3. assumes repository context instead of reteaching the architecture;
4. uses compact paragraphs, with Markdown only where it improves readability;
5. links the originating ticket;
6. contains no verification checklist, file inventory, diff-size justification, or stock scope section; and
7. may mention the removed heartbeat only if its consequence is material to understanding the design or resulting product.

The target is not a fixed template or word count. It is a concise, reviewer-useful explanation whose detail is earned by motivation, behaviour, design, or risk.
