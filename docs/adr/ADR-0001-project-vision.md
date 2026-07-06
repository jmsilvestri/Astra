# ADR-0001: Project Vision and Founding Principles

## Status

Accepted

## Date

2026-07-06

## Context

Astra is being created as an open source, local-first AI voice assistant. The project needs clear founding principles before implementation begins so future contributors can make consistent decisions about architecture, integrations, privacy, and product behavior.

Mainstream voice assistants are often cloud-dependent, limited in reasoning, and difficult for users to inspect or modify. Astra should explore a different model: a personal assistant that can run locally where possible, avoid per-token runtime costs, and remain modular enough for users and contributors to adapt.

## Decision

Astra will be built around these founding principles:

1. Privacy First
2. Local First
3. Zero Token Cost Runtime
4. Modular by Design
5. Open by Default
6. User Delight over Feature Count

The primary runtime must not depend on paid token APIs. Local reasoning through Ollama is the initial direction. Voice, tools, memory, and integrations should be designed as replaceable modules.

## Consequences

This decision means:

- The project may reject convenient integrations if they create runtime token costs or privacy risks.
- Architecture work must prioritize clear boundaries and replaceable components.
- Documentation is part of the product, not an afterthought.
- Feature growth should be slower but more coherent.
- Contributors have a clear basis for evaluating technical and product tradeoffs.

This decision does not prevent optional integrations, experiments, or development tooling, but the core Astra runtime must remain aligned with the founding principles.
