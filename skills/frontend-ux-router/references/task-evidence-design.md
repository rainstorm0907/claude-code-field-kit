# Task Evidence Design

Use this reference for evidence-based judgment and actions that depend on people, objects and versions staying connected: review, moderation, labeling, previews, generated results, calculations, media, charts and timelines. Apply the common authority, observation and completion contract in `frontend-creation.md`.

## Contents

- [Frame the decision](#frame-the-decision)
- [Present decision evidence](#present-decision-evidence)
- [Keep the decision loop together](#keep-the-decision-loop-together)
- [Use familiar encodings](#use-familiar-encodings)
- [Prototype one complete unit](#prototype-one-complete-unit)
- [Verify dynamic relationships](#verify-dynamic-relationships)
- [Preserve the loop across viewports](#preserve-the-loop-across-viewports)
- [Return to the task model](#return-to-the-task-model)
- [Completion evidence](#completion-evidence)

## Frame the decision

Use the established path. Start from the actor's verb, such as compare, choose, correct or approve, and identify the evidence needed for that judgment, the action and its visible result. Map internal categories to judgments the person can actually make. Preserve a legitimate uncertainty action and the relevant recovery, interruption, resume and completion paths.

## Present decision evidence

- Match the medium to the judgment: editable object with result, comparable states together, source with review criteria, or calculation inputs with value and consequence.
- When timing matters, synchronize source media and visualization.
- Use summaries, counts and metadata for orientation; keep diagnostics, internal taxonomy, confidence semantics and storage fields in development or expert surfaces.

When judging generated text, expose the source and the result together where the
meaning can change a decision. Preserve actor, time and certainty: a plan must
not turn into a confirmed event, and past work must not become a future task
without evidence. Structural validity and matching citations do not prove the
sentence's meaning. Surface relevant late-arriving or corrected evidence where
the person makes that decision; do not bury it below unchanged history.

If evidence changes after a draft was generated, identify the draft's source
version or stale state. Let the person compare and selectively apply useful
changes while preserving their edits. An empty-fields-only apply action needs a
visible correction path when existing content is the part that needs updating.

## Keep the decision loop together

Keep orientation, current state, evidence, question, actions, feedback and continuation in one working context; this is not a mandatory screen order.

- Preserve transient evidence and playback, selection, comparison or preview context when the layout stacks.
- Offer a plain uncertainty action where evidence allows multiple interpretations, with the relevant undo, correction and retry paths.
- Keep expert diagnostics behind a deliberate entry; leave primary-task prerequisites discoverable.
- For batch actions, show the selected scope and ineligible items before execution. Offer an in-context way to exclude or resolve them where allowed; never steer a valid deferred decision into approval just to enable the button. Preserve the product's atomic or partial-processing contract.
- Distinguish request accepted, still processing, result ready, applied and saved when those states affect the next action. Make a ready result reachable. Do not return to a misleading idle prompt when processing completes.
- Incoming questions or review requests must appear at the responsible role's entry point and remain connected to the relevant item. Reading, accepting responsibility and completing work are distinct events; create only the actions the agreed product supports.

## Use familiar encodings

Use color, icons, sound, motion and labels with familiar domain meaning. Start with neutral emphasis for a moment or object; add a distinct encoding only when that distinction helps the decision. Keep it adjacent to evidence, persistent while needed, understandable and accessible through more than one sensory channel. Observe whether it reduces cognitive work in the rendered task.

## Prototype one complete unit

Choose a representative item, comparison or connected sequence, including the before/after relationship the judgment needs. Exercise its relevant action or viewing experience and result under `frontend-creation.md` §§9–10. Expand batch mechanics only when the assignment needs them.

## Verify dynamic relationships

Verify product verbs as observed state transitions:

| Relationship | Evidence |
|---|---|
| selection -> preview | selected input and rendered preview correspond |
| edit -> result | visible result reflects the current input |
| action -> feedback | action produces clear progress and final status |
| error -> recovery | safe input and context remain available for retry |
| save -> resume | reload restores the confirmed state |
| source media -> visualization | playback, seeking, and end state remain synchronized |
| item change -> context | evidence, actions and feedback refer to the same current item |
| role change -> actor | recorded identity and authority belong to the person acting, not an inherited form value |
| response -> recipient | the responsible role can find it from their starting view |
| version change -> response | identity, object and version still identify the actual read, question or decision |
| new evidence -> review | relevant statuses show the impact; older proposals are distinguishable |
| revision -> change claim | the claim matches actual changed fields, not merely a new version or review flag |

When several roles share a session, keep actor identity and role-specific input
separate. Reuse a known authenticated identity only when it is still the actual
actor; do not borrow the last author's name to satisfy another role's required
field. Check shared-session role switching as well as a fresh session when this
risk exists.

Distinguish new evidence, reviewed evidence and changed output. If renewed review
is required, record the actual correction or an explicit no-change decision tied
to that evidence; a generic checkmark alone must not claim that the new content
was incorporated. Preserve earlier released versions and their responses. Show
the meaningful change at the granularity needed for the task; full sentence-by-sentence
diff and new acceptance features are not universal requirements.

For temporal interfaces, exercise the supported transitions affected by the change, such as play, seeking, end/reset or resume. Do not invent controls just to complete this list. Measure relevant synchronization and distinguish sampled frames from full-speed observation.

## Preserve the loop across viewports

- Inspect the real target viewport and a materially narrower viewport.
- Keep evidence, question, and action together when the decision depends on transient context.
- Preserve content priority, playback or selection context, and the primary action while stacking.
- Check overflow, wrapping, sticky collisions, zoom, and viewport-specific controls.
- Keep progress proportional to the task and secondary to the current decision.

## Return to the task model

Revisit the task or implementation cause when:

- people need repeated coaching, a private legend or internal categories to know what to do;
- explanations or metadata replace evidence the product could show;
- evidence and action separate, or related media, previews, calculations, totals and states move independently;
- an interaction step is missing, or repeated copy, queue-size and polish changes leave the same task unclear.

Use the specific failure to choose local repair or a different task structure under `frontend-creation.md`. Extra explanation cannot substitute for a missing relationship; a local defect need not restart the whole design.

## Completion evidence

In the existing result record, retain the decisive route, fixture and viewports; evidence, action and result; relevant uncertainty, recovery and resume paths; observed dynamic relationships and synchronization; and affected keyboard/focus, browser errors or overflow. Include screenshots or traces only when permitted.

Use `frontend-creation.md` §9 for allowed observation, deferred checks and code-versus-screen evidence. Do not create another report or status ladder.
