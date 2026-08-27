---
name: academic-paper
description: 12-agent academic paper writing pipeline. 11 modes including full/plan/outline/revision/revision-coach/abstract/lit-review/format-convert/citation-check/disclosure/rebuttal-audit. Supports IMRaD, literature review, case study, theoretical paper, policy brief, conference paper. 5 citation formats (APA 7/Chicago/MLA/IEEE/Vancouver). Output: LaTeX/PDF/DOCX/Markdown. Triggers on: write paper, academic paper, paper outline, revise paper, check citations, convert format, guide my paper, parse reviews, AI disclosure, 寫論文, 學術論文, 論文大綱, 修改論文, 轉換格式, 引導我寫論文, 審查意見
---

# Academic Paper — Paper Writing Agent Team

12-agent pipeline for academic paper writing, all disciplines, higher education as default reference. Based on Academic Research Skills v3.2.0 by Cheng-I Wu (CC-BY-NC 4.0).

## Quick Start
```
Write a paper on the impact of AI on higher education quality assurance
引導我寫論文：少子化對私立大學經營策略的影響
```

## 11 Modes

| Mode | Trigger | Output |
|------|---------|--------|
| `full` | "Write a paper" | Complete draft + figures + bilingual abstract |
| `plan` | "Guide my paper" / "Help me plan" | Chapter Plan + INSIGHT Collection |
| `outline-only` | "Paper outline" | Detailed outline + evidence map |
| `revision` | "Revise paper" + draft + review comments | Patch-applied revised draft + Response to Reviewers |
| `revision-coach` | "Parse reviews" / "Revision roadmap" | Structured Revision Roadmap (no draft generated) |
| `abstract-only` | "Write abstract" | Bilingual abstract (zh-TW + EN) + keywords |
| `lit-review` | "Literature review paper" | Annotated bibliography + synthesis |
| `format-convert` | "Convert to LaTeX/IEEE/Chicago" | Formatted document + LaTeX/PDF |
| `citation-check` | "Check citations" | Citation error report |
| `disclosure` | "AI disclosure for Nature/NeurIPS" | Venue-specific AI usage statement |
| `rebuttal-audit` | "Audit my response" (requires BOTH reviews AND existing draft) | Rebuttal QA report — advisory only, no content generation |

## 12-Agent Team

| # | Agent | Phase |
|---|-------|-------|
| 1 | intake_agent | Phase 0 — Configuration interview |
| 2 | literature_strategist_agent | Phase 1 — Search strategy + sources |
| 3 | structure_architect_agent | Phase 2 — Outline + evidence map |
| 4 | argument_builder_agent | Phase 3 — Claim-evidence chains |
| 5 | draft_writer_agent | Phase 4 — Full draft writing |
| 6 | citation_compliance_agent | Phase 5a — Citation audit |
| 7 | abstract_bilingual_agent | Phase 5b — Bilingual abstract |
| 8 | peer_reviewer_agent | Phase 6 — Simulated review |
| 9 | formatter_agent | Phase 7 — LaTeX/DOCX/PDF output |
| 10 | socratic_mentor_agent | Plan mode — Chapter-by-chapter guidance |
| 11 | visualization_agent | Phase 4/7 — Publication-quality figures |
| 12 | revision_coach_agent | Revision-coach mode — Parse reviewer comments |

## 8-Phase Workflow

**Phase 0:** Configuration interview → Paper Configuration Record → **User confirmation**
**Phase 1:** Literature search + source corpus
**Phase 2:** Architecture design → Outline + evidence map → **User approval**
**Phase 3:** Argumentation construction
**Phase 4:** Full-text drafting (section-by-section)
**Phase 5a/b (parallel):** Citations audit + Bilingual abstract
**Phase 6:** Peer review (max 2 revision loops)
**Phase 7:** Output formatting → LaTeX/PDF/DOCX/Markdown

## Output Formats

- **Text:** LaTeX (.tex + .bib), DOCX (via Pandoc), PDF (via tectonic), Markdown
- **Figures:** Python (matplotlib/seaborn) or R (ggplot2), colorblind-safe palettes
- **Citation Formats:** APA 7.0 (default), Chicago, MLA 9, IEEE, Vancouver

## Paper Structures

IMRaD (empirical), Thematic literature review, Theoretical analysis, Case study, Policy brief, Conference paper

## IRON RULES

1. User must confirm Paper Configuration Record before Phase 1
2. Max 2 revision loops; unresolved items → "Acknowledged Limitations"
3. Every paper MUST include: Data Availability, Ethics Declaration, CRediT author contributions, COI, Funding, AI disclosure, Limitations
4. Zero citation orphans — in-text ↔ reference list must perfectly match
5. Every citation must be verified via DOI or WebSearch
6. Fabricated citations are FORBIDDEN
7. DOI inclusion required for every source with a DOI
8. Bilingual abstracts independently composed (NOT mechanical translation)

## Anti-Patterns

- AI-typical terms ("delve into", "crucial"), em dash abuse, throat-clearing openers, uniform paragraph lengths
- Sycophantic revision — use REVIEWER_DISAGREE when justified
- Scope creep during revision

## Handoff from deep-research

Intake agent auto-detects: RQ Brief, Bibliography, Synthesis, INSIGHT Collection → skips redundant steps.

## Key References

- `references/apa7_extended_guide.md` — Full APA 7 reference
- `references/writing_quality_check.md` — AI-typical pattern detection
- `references/paper_structure_patterns.md` — 6 paper types
- `references/citation_format_switcher.md` — Format conversion rules
- `references/failure_paths.md` — 12 scenarios
- `templates/imrad_template.md` — IMRaD template
- `templates/latex_article_template.tex` — LaTeX template
- `agents/*.md` — Full agent definitions (12 agents)
