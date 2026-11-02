# Runtime — Claude Code

*Lead and teammates.* What the harness supplies. This skill still owns scope,
responsibility, approved staffing, evidence and completion. Tool names below match
Claude Code 2.1; the tool schema in your session wins over this table.

| Concern | Where it lives |
|---|---|
| Lead | the session the user is talking to |
| Approved teammate | the Agent tool with a `name` and `subagent_type: "workstream-owner"` or `"independent-verifier"` |
| Focused support | the Agent tool without a `name`: an ordinary subagent, not a roster member |
| Peer message, follow-up or correction | `SendMessage` with `to: "<name>"`; a finished background subagent continues with its agent ID |
| Shared task list | `TaskCreate`, `TaskList`, `TaskUpdate` (`owner` assigns a task) |
| Roster and status | `ListAgents` |
| Stop one going the wrong way | `TaskStop` with the teammate's name |
| Parallel spawn | several Agent calls in **one** message start together; calls in separate messages run one behind another |

Address peers by name. The lead is not a relay.

## Teams need the experimental flag

Agent teams are on only when `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` is set
(environment, or `env` in `~/.claude/settings.json`). `teammateMode` chooses how
teammates are shown (`in-process`, `tmux`, `iterm2` or `auto`). Without the flag,
the same contracts still work through ordinary subagents: the lead holds the
roster in its own notes, and an owner's follow-up goes through `SendMessage` to the
same agent where available.

## Limits that change the plan

- Teammates cannot spawn teammates. They can run ordinary subagents under their
  own authority.
- In-process teammates run subagents synchronously, not in the background.
- Teammates share the checkout. Give each owner a distinct write boundary; a
  verifier's "do not modify" is an instruction, not a sandbox.

## Roles

`agents/workstream-owner.md` and `agents/independent-verifier.md` (installed to
`~/.claude/agents/`) carry the matching contract from `teammate/` plus
Skill(dispatched). Send the task-specific brief, not a second copy of the
contract. If the agent type is missing, point the teammate at its contract path
in this skill and Skill(dispatched), and say that automatic role loading was
unavailable.

For a cold review, give the verifier the artifacts, environment constraints and
acceptance criteria, without the builder's reasoning or desired verdict.

Role files leave the model unset; the lead picks it per task through
Skill(model-guide).
