# Architecture

Astra's architecture should stay modular, replaceable, and understandable. Each major capability should live behind clear boundaries so the project can evolve without locking itself to one provider, model, or integration.

## Target Modules

## `astra_core`

Core orchestration for the assistant.

Responsibilities may include:

- Assistant loop coordination.
- Request routing.
- Conversation state.
- Tool invocation flow.
- High-level error handling.

`astra_core` should coordinate modules without owning every implementation detail.

## `astra_voice`

Voice input and output.

Responsibilities may include:

- Wake word handling.
- Moshi integration.
- Fallback speech-to-text.
- Fallback text-to-speech.
- Audio input and output interfaces.

Voice components should be replaceable so the project can support different local and hybrid options.

## `astra_llm`

Language model and reasoning layer.

Responsibilities may include:

- Ollama integration.
- Prompt templates.
- Model configuration.
- Tool-calling decisions.
- Response generation.

The primary runtime must not depend on paid token APIs.

## `astra_tools`

Tool integrations and external actions.

Potential tools include:

- Weather.
- Traffic.
- Gmail.
- Calendar.
- Spotify.
- Home Assistant.
- Web search.

Tools should be optional, documented, and isolated from core assistant logic.

## `astra_memory`

Local memory and user context.

Responsibilities may include:

- Local storage.
- Memory policies.
- Retrieval.
- User inspection and deletion.
- Privacy-preserving defaults.

Memory must be designed with user control and transparency from the beginning.

## `astra_config`

Configuration loading and validation.

Responsibilities may include:

- Environment variables.
- Local configuration files.
- Safe defaults.
- Validation and helpful errors.

Private values should live in `.env` files and must not be committed.

## `docs`

Project documentation.

Responsibilities include:

- Product vision.
- Roadmap.
- Architecture.
- ADRs.
- Engineering briefs.
- Contribution guidance.

Documentation should explain why decisions exist, not only what files contain.

## `tests`

Automated tests.

Responsibilities include:

- Unit tests for business logic.
- Integration tests where useful.
- Regression tests for fixed bugs.
- Contract tests for modular boundaries when needed.

Tests should grow as implementation begins.

## Architectural Rules

- Keep modules loosely coupled.
- Prefer local-first implementations.
- Make providers replaceable.
- Avoid unnecessary dependencies.
- Keep secrets out of source control.
- Document long-lived decisions with ADRs.
- Add tests when behavior is implemented.
