# Astra

Astra is an open source, local-first AI voice assistant project. It is intended to become a smarter, more private alternative to cloud voice assistants such as Alexa or Google Home, with natural conversation, modular capabilities, and reasoning that can run locally.

The project is in its initial foundation phase. Sprint 0 focuses on documentation, project structure, and shared engineering principles. No production assistant behavior is implemented yet.

## Philosophy

Astra is guided by a small set of founding principles:

1. Privacy First
2. Local First
3. Zero Token Cost Runtime
4. Modular by Design
5. Open by Default
6. User Delight over Feature Count

These principles matter more than adding features quickly. Astra should remain understandable, replaceable, and respectful of the people who run it in their homes.

## Target Capabilities

Astra is expected to grow toward:

- Natural text and voice conversation.
- Local reasoning through Ollama.
- Voice input and output with replaceable speech components.
- Tool calling for weather, traffic, calendar, email, music, home automation, and web search.
- Local memory that users can inspect and control.
- A modular architecture where components can be swapped without rewriting the product.

## Current Status

Astra is at Sprint 0: Foundation.

The repository currently contains project documentation and architectural direction only. Business logic, LLM integration, voice processing, tool calling, and memory features are intentionally out of scope for this phase.

## Installation

This project uses Python and `uv`.

```powershell
git clone https://github.com/jmsilvestri/Astra.git
cd Astra
uv sync
```

If dependencies have not been added yet, `uv sync` may only prepare the project environment.

## Running Tests

When tests are available, run:

```powershell
uv run pytest
```

Sprint 0 does not add business logic, so test coverage is expected to grow in later sprints as implementation begins.

## Documentation

Start here:

- [Product Vision](docs/PRODUCT_VISION.md)
- [Roadmap](docs/ROADMAP.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Contribution Guide](CONTRIBUTING.md)
- [Project History](PROJECT_HISTORY.md)

## Runtime Cost Policy

Astra must not depend on paid token APIs in its primary runtime. Codex and other development tools may be used to build the project, but Astra itself should be able to run without per-token costs.

## License

Astra is released under the MIT License.
