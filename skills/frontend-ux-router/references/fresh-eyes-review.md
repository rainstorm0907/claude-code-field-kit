# Fresh-Eyes Review Protocol

Use for a material first-reader comprehension question, or when the user or release contract requires independent review. It is not a compulsory stage of every visual edit and does not certify taste or whole-product quality.

The implementer prepares the evidence. A different reviewer starts without implementation coaching. Self-review must not be labeled independent.

## Evidence and environment

Apply `frontend-creation.md` §9 and the current platform restrictions before selecting an observation method. Send only:

1. one persona line in product language;
2. permitted rendered images at the relevant viewport(s), or a live route the reviewer is actually permitted and able to observe;
3. optionally, the post-action view when feedback is the question;
4. the observation/tool restrictions that must be obeyed.

Do not include the builder's task framing, design rationale, internal terminology, diff or desired verdict. Observation restrictions are essential instructions, not design coaching. A goal/quality review needs its own brief and must not be presented as this comprehension-only check.

When no browser automation or capture tool is available or permitted, do not ask an agent to improvise one. The user can inspect the screen under §9. Only a permitted rendered artifact supports an agent's visual review. A user's reported observations may support a scoped finding, but neither those notes nor source code make the agent an independent visual observer. If no allowed rendered evidence is available, return **NOT OBSERVED** and continue other assigned checks; do not invent a PASS or call missing evidence a UI failure.

## Reviewer prompt

Fill the evidence and observation boundary from actual capabilities. Do not insert an instruction to open a route when browsing or automation is forbidden.

```text
You are a first-time user of this product. You are: {PERSONA_LINE}.
Nobody will explain the design to you.
Evidence available for this review: {PERMITTED_RENDERED_EVIDENCE}.
Observation boundary: {ALLOWED_OBSERVATION_ONLY}.

Using only what is actually visible, answer:
1. What product or task is this?
2. What must you inspect, listen to or compare?
3. What is happening now?
4. What would you do first, including simply watching, and why?
5. What result do you expect after that action?
6. Which elements have a purpose you cannot explain?
7. Which strings read like implementation notes? Quote them.
8. What would you need to be taught before acting confidently?

Give PASS if 1-5 are clear from visible evidence and 6-8 contain no blocking
item. Give FAIL when the available screen requires a guess or has a blocking
comprehension problem, and identify the question and visible evidence.
Give NOT OBSERVED if rendered evidence cannot be accessed within the allowed
method. Do not substitute implementation knowledge or guesses for observation.
Write the findings in Korean unless the current task requires another language.
```

## Use the findings

Check each supported finding for an orientation, evidence, action, feedback or copy defect. Repair the relevant path under `frontend-creation.md`; do not coach the reviewer into agreement or hide a wrong task structure behind a tooltip. A known local defect needs a local repair.

Re-review only when required or changed evidence can affect acceptance. A required review stays pending until valid evidence resolves it. An optional unperformed review does not require another agent. Keep the actual result and observation scope in existing evidence.

## Dispatcher notes

Use a fresh context that has not seen the implementation brief. Follow the installed runtime and model permissions; observation quality is not guaranteed by a model label. Preserve role-specific expertise in the persona. Restrict the claim to the screen and state observed: a comprehension PASS does not establish interactions, data correctness, user taste or unobserved views.
