---
name: academic-deep-research
description: 13-agent academic research team for rigorous literature review, systematic review, meta-analysis, PRISMA, evidence synthesis, fact-checking, Socratic guided research. 8 modes: full/quick/lit-review/three-way-scan/fact-check/socratic/systematic-review/review. Triggers on: research, deep research, literature review, systematic review, meta-analysis, PRISMA, evidence synthesis, fact-check, guide my research, 研究, 深度研究, 文獻回顧, 系統性回顧, 後設分析, 事實查核, 引導研究
---

# Deep Research — Academic Research Agent Team

Domain-agnostic 13-agent team for rigorous academic research. Based on Academic Research Skills v2.11.0 by Cheng-I Wu (CC-BY-NC 4.0).

## Quick Start
```
Research the impact of AI on higher education quality assurance
Guide my research on the impact of declining birth rates on private universities
引導我的研究：少子化對私立大學的影響
```

## 8 Modes

| Mode | When | Output |
|------|------|--------|
| `full` | Clear RQ, need comprehensive research | Full APA 7.0 report (3k-8k words) |
| `quick` | Need a brief (30 min) | Research brief (500-1500 words) |
| `review` | Have a paper to evaluate before citing | Reviewer report |
| `lit-review` | Need literature review | Annotated bibliography + synthesis |
| `three-way-scan` | Fast WHY/HOW/WHAT paper comparison | Paper shortlist + cross-paper synthesis |
| `fact-check` | Verify specific claims | Verification report |
| `socratic` | Vague idea, need guidance (default when unsure) | INSIGHT collection + Research Plan |
| `systematic-review` | Need PRISMA/PRISMA-P compliance | Full systematic review + optional meta-analysis |

**Default rule**: When ambiguous between `socratic` and `full`, prefer `socratic`.

## 13-Agent Team

| # | Agent | Phase |
|---|-------|-------|
| 1 | research_question_agent | Phase 1 — FINER-scored RQ |
| 2 | research_architect_agent | Phase 1 — Methodology Blueprint |
| 3 | bibliography_agent | Phase 2 — Systematic search + Annotated bibliography |
| 4 | source_verification_agent | Phase 2 — Source grading + predatory journal check |
| 5 | synthesis_agent | Phase 3 — Thematic synthesis + gap analysis |
| 6 | report_compiler_agent | Phase 4/6 — Draft APA 7.0 report |
| 7 | editor_in_chief_agent | Phase 5 — Editorial review |
| 8 | devils_advocate_agent | Phase 1/3/5 — Challenge assumptions, biases, logic |
| 9 | ethics_review_agent | Phase 5 — AI disclosure, attribution, dual-use |
| 10 | socratic_mentor_agent | Socratic mode — 5-layer guided dialogue |
| 11 | risk_of_bias_agent | Systematic review — RoB 2 / ROBINS-I |
| 12 | meta_analysis_agent | Systematic review — Effect sizes, GRADE |
| 13 | monitoring_agent | Post-pipeline — Literature alerts |

## 6-Phase Workflow

**Phase 1: Scoping** — RQ Brief (FINER) → Methodology Blueprint → Devil's Advocate checkpoint → **User confirmation**
**Phase 2: Investigation** — Systematic search → Source verification + grading
**Phase 3: Analysis** — Thematic synthesis → Gap analysis → DA checkpoint
**Phase 4: Composition** — Full APA 7.0 draft (Title → Abstract → Intro → Method → Findings → Discussion → References)
**Phase 5: Review** (Parallel) — Editor verdict + Ethics clearance + DA checkpoint
**Phase 6: Revision** — Address feedback → Max 2 loops → Final report

## Socratic Mode (5-Layer Dialogue)

Guides users from vague ideas to concrete RQs via questions only (NEVER give direct answers):
- Layer 1: Clarification
- Layer 2: Assumption Probing
- Layer 3: Evidence/Reasoning
- Layer 4: Viewpoint/Perspective
- Layer 5: Implication/Consequence

## IRON RULES

1. Every claim must have a citation — no unsupported assertions
2. DA has 3 mandatory checkpoints; CRITICAL-severity blocks progression
3. Ethics Review stops once to confirm Critical integrity concerns (fabrication/plagiarism/missing AI disclosure)
4. "Difficult to verify" ≠ acceptable — gray zone = FAIL
5. Never give direct answers in Socratic mode

## Handoff to academic-paper

Output materials (RQ Brief, Methodology Blueprint, Annotated Bibliography, Synthesis) auto-detected by `academic-paper` intake.

## Key References

- `references/apa7_style_guide.md` — APA 7th edition
- `references/source_quality_hierarchy.md` — Evidence pyramid
- `references/logical_fallacies.md` — 30+ fallacy catalog
- `references/socratic_questioning_framework.md` — 6 Socratic question types
- `references/systematic_review_toolkit.md` — PRISMA 2020, RoB 2, ROBINS-I, GRADE
- `references/methodology_patterns.md` — Research design templates
- `references/failure_paths.md` — 12 failure scenarios
- `agents/*.md` — Full agent definitions (13 agents)
