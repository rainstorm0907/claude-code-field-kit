---
name: model-guide
description: "Use when choosing a model for delegated work in Claude Code: subagents, agent-team owners and independent verifiers."
---

# Model guide

The user chooses the lead model; never change it automatically. Roles describe
responsibility, not fixed models. Read `../dispatching/SKILL.md` first: if an
agent already worked on this problem, continuing it usually beats a new model.

## Route by the hardest part

An owner keeps judgment, diagnosis, implementation, correction and proof for one
outcome. Workers take bounded maps, evidence gathering and settled execution. Do
not hand unresolved judgment to a cheap worker merely to fit a budget.

| Role | Default |
|---|---|
| Owner | `inherit` (the lead's model) or `opus`; `fable` for hard framing or structure when the user's plan has it |
| Worker | `sonnet`; `haiku` for simple search, extraction or file maps |
| Verifier | a fresh capable context (`opus` or `sonnet`); a different model adds diversity, not independence by itself |

Match the work, not a permanent job title. Keep diagnosis with the owner while the
explanation is still uncertain.

## Settings

The Agent tool's `model` takes an alias (`fable`, `opus`, `sonnet`, `haiku`), a
full model ID, or `inherit`. Omitting it uses the configured default subagent
model, else the lead's. Use an exact ID only when the user gave or confirmed it;
try it once, report the actual error on failure, and never switch models silently.
Report the requested model separately from what the runtime confirms.

## Approval

- Before forming a team or running many agents, tell the user roughly how many
  agents and runs, and which models. Go once they agree.
- Corrections, retries and re-verification of an approved owner's same outcome
  continue under that approval. A new outcome, a costlier model or a larger
  roster is a new question.
- Other routes (another CLI, a proxy, an external provider) only when the user set
  them up and asked for them.
