# Astra

Astra is an open source, local-first AI voice assistant project. It is intended to become a smarter, more private alternative to cloud voice assistants such as Alexa or Google Home, with natural conversation, modular capabilities, and reasoning that can run locally.

The project is in its early implementation phase. Sprint 0 established the foundation documentation. Sprint 1 introduces the first text assistant loop backed by a local Ollama runtime.

## Philosophy

Astra is guided by a small set of founding principles:

1. Privacy First
2. Local First
3. Zero Token Cost Runtime
4. Modular by Design
5. Open by Default
6. User Delight over Feature Count

These principles matter more than adding features quickly. Astra should remain understandable, replaceable, and respectful of the people who run it in their homes.

## Current Capabilities

Astra currently includes:

- A command-line text assistant loop.
- Local Ollama-backed response generation.
- Environment-based configuration through `.env`.
- A replaceable LLM client boundary.
- Focused tests for assistant behavior and settings.

## Target Capabilities

Astra is expected to grow toward:

- Natural text and voice conversation.
- Local reasoning through Ollama.
- Voice input and output with replaceable speech components.
- Tool calling for weather, traffic, calendar, email, music, home automation, and web search.
- Local memory that users can inspect and control.
- A modular architecture where components can be swapped without rewriting the product.

## Current Status

Astra is at Sprint 1: Text Assistant.

The assistant can run as a local text loop, but tool calling, voice, memory, and personal integrations are intentionally not implemented yet.

## Installation

This project uses Python and `uv`.

```powershell
git clone https://github.com/jmsilvestri/Astra.git
cd Astra
uv sync
```

Copy the example environment file if you want to customize local settings:

```powershell
Copy-Item .env.example .env
```

Default settings expect Ollama at `http://localhost:11434` using the `llama3.2` model.

## Running Astra

Start Ollama locally and make sure the configured model is available. For the default model:

```powershell
ollama pull llama3.2
ollama serve
```

In another terminal, run:

```powershell
uv run astra
```

Type `exit`, `quit`, or `q` to stop the assistant.

## Running Tests

Run:

```powershell
uv run pytest
```

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
