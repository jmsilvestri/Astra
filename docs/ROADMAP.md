# Roadmap

This roadmap describes the intended project direction. It may change as the project learns from implementation and users.

## Sprint 0 - Foundation

Establish the professional open source foundation:

- README.
- License.
- Contribution guide.
- Agent instructions.
- Product vision.
- Roadmap.
- Architecture overview.
- Initial ADR.
- Sprint brief.

No business logic is included in this sprint.

## Sprint 1 - Text Assistant

Create the first text-based assistant loop:

- Local command-line interaction.
- Initial prompt structure.
- Ollama-backed reasoning.
- Basic configuration loading.
- Tests for core assistant flow.

## Sprint 2 - Tool Calling

Introduce a modular tool system:

- Tool registry.
- Tool schemas.
- Safe tool execution boundaries.
- Initial example tools.
- Tests for tool selection and execution.

## Sprint 3 - Voice Layer

Add voice input and output:

- Wake word direction.
- Moshi research and integration path.
- Fallback STT/TTS options.
- Voice interaction loop.
- Replaceable voice interfaces.

## Sprint 4 - Memory

Add local memory:

- User-controlled storage.
- Memory read/write policies.
- Transparent inspection.
- Privacy-preserving defaults.
- Tests for memory behavior.

## Sprint 5 - Personal Integrations

Add useful integrations:

- Weather.
- Traffic.
- Gmail.
- Calendar.
- Spotify.
- Home Assistant.
- Web search.

Each integration should be optional, documented, and replaceable.

## Sprint 6 - Delightful Assistant

Refine the assistant experience:

- Better conversational behavior.
- Proactive but respectful assistance.
- Personality and tone guidelines.
- Error recovery.
- User delight improvements.
- Documentation for real-world setup.
