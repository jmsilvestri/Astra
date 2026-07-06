# Contributing to Astra

Thank you for considering a contribution to Astra. This project is early, and the most valuable contributions are clear, focused, and aligned with the project principles.

## Workflow

1. Read the project documentation.
2. Create a focused branch.
3. Make the smallest useful change.
4. Add or update documentation when behavior, architecture, or setup changes.
5. Add tests when code behavior is introduced or changed.
6. Open a pull request with a clear explanation of the change.

## Recommended Branches

Use descriptive branch names:

- `docs/project-foundation`
- `feature/text-assistant`
- `fix/config-loading`
- `adr/local-memory`

## Commit Conventions

Prefer simple conventional commits:

- `docs: update roadmap`
- `feat: add text assistant shell`
- `fix: handle missing config file`
- `test: cover tool registry`
- `chore: update project metadata`

Keep commits focused. A commit should be easy to review and revert if needed.

## Quality Expectations

Contributions should:

- Respect Astra's founding principles.
- Avoid paid token APIs in the primary runtime.
- Keep modules replaceable and understandable.
- Avoid unnecessary dependencies.
- Avoid committing secrets.
- Favor readable code and clear documentation over cleverness.

## Tests

When tests exist, run:

```powershell
uv run pytest
```

New business logic should include focused tests. Documentation-only changes may not need tests.

## Documentation

Update documentation when you change:

- User-facing behavior.
- Setup or configuration.
- Architecture.
- Runtime assumptions.
- Project direction.

Long-lived architectural decisions should be captured as ADRs in `docs/adr/`.

## Pull Request Process

Pull requests should include:

- What changed.
- Why it changed.
- How it was validated.
- Any follow-up work or known limitations.

The project favors steady, understandable progress over large unreviewable changes.
