# Sprint 000: Foundation

## Context

Astra is starting as an open source, local-first AI voice assistant project. Before implementing assistant behavior, the repository needs a professional foundation that explains what the project is, why it exists, how contributors should work, and what architectural direction should guide future development.

## Objective

Create the initial project documentation and decision records for Astra without adding business logic, heavy dependencies, voice integrations, LLM integrations, or tool implementations.

## Deliverables

- `README.md`
- `LICENSE`
- `AGENTS.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `PROJECT_HISTORY.md`
- `docs/PRODUCT_VISION.md`
- `docs/ROADMAP.md`
- `docs/ARCHITECTURE.md`
- `docs/adr/ADR-0001-project-vision.md`
- `docs/engineering/SPRINT-000-foundation.md`

## Out of Scope

- Business logic.
- Ollama integration.
- Moshi integration.
- Weather, traffic, email, calendar, music, or home automation tools.
- Voice input or output.
- Memory implementation.
- Heavy dependencies.
- Paid token API integration in the primary runtime.

## Acceptance Criteria

Sprint 000 is complete when:

- All listed files exist.
- The README clearly explains the project.
- The founding principles are documented.
- A new contributor can understand the project direction in under 15 minutes.
- No business logic has been added.
- No unnecessary dependency has been added.
- No secret is present.
- File paths are coherent.
- Documentation is written in English.
- The content is simple, professional, and suitable for an open source project.

## Validation Checklist

- [x] Confirm all deliverables exist.
- [x] Confirm documentation is in English.
- [x] Confirm no runtime OpenAI API integration exists.
- [x] Confirm no secrets are committed.
- [x] Confirm no business logic was added.
- [x] Confirm no unnecessary dependencies were added.
- [x] Confirm architecture documentation describes the target modules.
- [x] Confirm the ADR is accepted and dated.

## Risks

- The project could grow too quickly before its boundaries are clear.
- Runtime integrations could accidentally introduce token costs.
- Voice and tool features could become tightly coupled to early provider choices.
- Documentation could drift from implementation if it is not maintained.
- Memory features could create privacy risks if not designed carefully.

The foundation sprint reduces these risks by establishing clear principles and a shared project direction before implementation begins.
