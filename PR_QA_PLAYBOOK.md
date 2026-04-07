# Cost-Aware PR QA Playbook (Web + Visual)

This repository uses a cost-aware QA strategy for UI and visual component changes.

## Goal
Catch regressions reliably while minimizing screenshot/image-processing costs for autonomous agents.

## Blocking QA (required for merge)
1. Build, lint, and type checks pass.
2. Unit tests pass for changed modules.
3. Integration tests pass for changed feature flows.
4. DOM/state assertions validate expected behavior for UI changes.

## Visual QA Policy (selective screenshots)
Use screenshots only when one of these applies:
1. Layout/CSS/spacing/typography changed.
2. Rendering differs by viewport or breakpoint.
3. Canvas/SVG/chart output changed.
4. A known visual bug is being fixed.

If none apply, prefer deterministic assertions over screenshots.

## Screenshot Budget (when required)
Capture only these states:
1. Happy path
2. One edge state
3. One error state
4. One mobile breakpoint

Maximum default: 4 screenshots per changed feature.

## Agent Workflow
1. Navigate using scripted steps (stable selectors) so runs are reproducible.
2. Assert DOM/state first.
3. Capture screenshots only if visual criteria above are met.
4. Attach a short QA summary to the PR:
   - checks run
   - assertions passed
   - screenshots captured (or reason skipped)

## Flake Handling
1. On first failure, rerun once to detect flakiness.
2. If flaky, mark non-blocking and open a fix issue.
3. Keep flaky tests out of merge gates until stabilized.

## Escalation to Human Review
Require human QA when:
1. Accessibility-critical UI changed.
2. Design-system tokens/components changed broadly.
3. Screenshot diffs are ambiguous.

