# Agent Instructions

These instructions apply to Codex and any other development agent working on Astra.

## Project Principles

Astra is a local-first, privacy-first open source voice assistant. All changes must respect the founding principles:

1. Privacy First
2. Local First
3. Zero Token Cost Runtime
4. Modular by Design
5. Open by Default
6. User Delight over Feature Count

## Before Implementing

- Read the relevant project documentation before changing code.
- Start with `README.md`, `docs/PRODUCT_VISION.md`, `docs/ROADMAP.md`, and `docs/ARCHITECTURE.md`.
- Prefer small, focused changes that keep the project easy to understand.
- Do not add business logic during foundation-only work.

## Runtime Constraints

- Do not integrate paid token APIs into Astra's primary runtime.
- Do not add OpenAI API usage to the runtime assistant path.
- Development tools may use Codex, but Astra itself must remain able to run without per-token costs.
- Prefer local and replaceable components.

## Secrets and Configuration

- Never commit secrets, tokens, passwords, private keys, or personal credentials.
- Use `.env` for private local variables.
- Keep example configuration safe and clearly non-secret.

## Architecture

- Preserve modular boundaries between core orchestration, voice, LLM, tools, memory, and configuration.
- Avoid coupling modules to one provider or one external service.
- Design integrations so they can be replaced later.

## Documentation and Tests

- Document important decisions and meaningful changes.
- Update ADRs when a lasting architectural decision is made.
- Add tests when business logic is introduced.
- Keep documentation accurate enough for a new contributor to understand the project quickly.
