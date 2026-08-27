---
name: academic-pipeline
description: Orchestrator for the complete academic research-to-publication pipeline. Coordinates deep-research, academic-paper, and academic-paper-reviewer into a 10-stage workflow with mandatory integrity gates, adaptive checkpoints, and two-stage peer review. Triggers on: academic pipeline, research to paper, full paper workflow, paper pipeline, end-to-end paper, research-to-publication, complete paper workflow, 論文管線, 研究到出版, 完整論文流程
---

# Academic Pipeline — Full Research Workflow Orchestrator

Lightweight orchestrator managing the complete pipeline from research to final manuscript. Detects stages, recommends modes, dispatches skills, manages transitions, tracks state. Based on Academic Research Skills v3.13.0 by Cheng-I Wu (CC-BY-NC 4.0).

## Quick Start
```
I want to write a research paper on the impact of AI on higher education
I already have a paper, help me review it
I received reviewer comments, help me revise
我想做一篇關於 AI 對高教品保影響的研究論文
```

## 10 Pipeline Stages

| Stage | Name | Skill Dispatched | Key Deliverables |
|-------|------|-----------------|-----------------|
| 1 | RESEARCH | `academic-deep-research` (socratic/full/quick) | RQ Brief, Methodology, Bibliography, Synthesis |
| 2 | WRITE | `academic-paper` (plan/full) | Paper Draft |
| **2.5** | **INTEGRITY** | integrity_verification agent | **Verification report + corrected paper (MANDATORY)** |
| 3 | REVIEW | `academic-paper-reviewer` (full) | 5 review reports + Editorial Decision |
| 4 | REVISE | `academic-paper` (revision) | Revised Draft + Response to Reviewers |
| **3'** | **RE-REVIEW** | `academic-paper-reviewer` (re-review) | **Verification + R&R traceability matrix** |
| **4'** | **RE-REVISE** | `academic-paper` (revision) | **Second revised draft (if needed)** |
| **4.5** | **FINAL INTEGRITY** | integrity_verification agent | **Final verification — MUST pass 100%** |
| 5 | FINALIZE | `academic-paper` (format-convert) | Final Paper (MD → DOCX → LaTeX → PDF) |
| **6** | **PROCESS SUMMARY** | Orchestrator (auto) | Creation process record + collaboration quality evaluation |

## State Machine

```
Stage 1 → [confirm] → Stage 2 → [confirm] → Stage 2.5
Stage 2.5 → PASS → Stage 3 | FAIL → fix+re-verify (max 3 rounds)
Stage 3 → Accept → Stage 4.5 | Minor/Major → Stage 4 | Reject → Stage 2 or end
Stage 4 → [confirm] → Stage 3'
Stage 3' → Accept/Minor → Stage 4.5 | Major → Stage 4'
Stage 4' → [confirm] → Stage 4.5 (no return to review)
Stage 4.5 → PASS → Stage 5 | FAIL → fix+re-verify
Stage 5 → MD → DOCX → LaTeX → confirm → PDF → Stage 6
Stage 6 → Process record (bilingual MD + PDF) → END
```

## Adaptive Checkpoint System

| Type | When | Behavior |
|------|------|----------|
| FULL | First checkpoint, integrity boundaries, before finalization | Full deliverables + decision dashboard + all options |
| SLIM | After 2+ consecutive "continue" | One-line status + continue/pause |
| MANDATORY | Integrity FAIL, Review decision, Stage 5 | Cannot be skipped; explicit input required |

**IRON RULE**: After each stage, proactively prompt and wait for user confirmation.

## 5 Orchestrator Agents

| # | Agent | Role |
|---|-------|------|
| 1 | pipeline_orchestrator_agent | Main dispatcher: detect stage, recommend mode, trigger skill |
| 2 | state_tracker_agent | Record completed stages, materials, revision count |
| 3 | integrity_verification_agent | 100% reference/citation/data verification (blocking gate) |
| 4 | collaboration_depth_agent | Advisory observer — scores user-AI collaboration (NEVER blocks) |
| 5 | claim_ref_alignment_audit_agent | Opt-in claim faithfulness audit (ARS_CLAIM_AUDIT=1) |

## Integrity Review (Stage 2.5 + 4.5)

5-phase verification: References → Citation context → Statistical data → Originality → Claims
- 7-mode AI Research Failure Mode Checklist (Lu 2026, Nature)
- PRISMA-trAIce + RAISE compliance check
- Stage 4.5 MUST pass with ZERO issues

## Mid-Entry Protocol

Users can enter from any stage. Orchestrator detects available materials and identifies gaps:
- "I already have a paper" → starts at Stage 2.5 (integrity)
- "I have review comments" → starts at Stage 4 (revise)
- Stage 2.5 CANNOT be skipped — even mid-entry papers must pass integrity

## IRON RULES

1. Integrity checks (2.5, 4.5) are MANDATORY — cannot be auto-skipped
2. Orchestrator NEVER does substantive work — only dispatches and coordinates
3. All MANDATORY checkpoints require explicit user input
4. Stage 4.5 must verify from scratch (not just re-check Stage 2.5 findings)
5. Max 2 revision loops (Stage 4 + Stage 4'); delta < 3 pts → suggest stopping
6. R&R tracking table must account for EVERY reviewer concern

## Key References

- `references/pipeline_state_machine.md` — Complete state transitions
- `references/integrity_review_protocol.md` — 5-phase verification procedure
- `references/ai_research_failure_modes.md` — 7-mode failure checklist
- `references/two_stage_review_protocol.md` — Review flow details
- `references/external_review_protocol.md` — Human reviewer integration
- `references/process_summary_protocol.md` — Stage 6 protocol
- `agents/*.md` — Full agent definitions (5 agents)
