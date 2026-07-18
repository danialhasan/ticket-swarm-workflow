```markdown
# ticket-swarm-workflow Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `ticket-swarm-workflow` TypeScript codebase. It covers file organization, import/export styles, test structure, and common workflows to ensure consistency and maintainability across contributions.

## Coding Conventions

### File Naming
- Use **kebab-case** for all file names.
  - Example:  
    ```
    ticket-handler.ts
    user-utils.test.ts
    ```

### Import Style
- Use **relative imports** for referencing local modules.
  - Example:
    ```typescript
    import { processTicket } from './ticket-handler';
    ```

### Export Style
- Use **named exports** for all modules.
  - Example:
    ```typescript
    // ticket-handler.ts
    export function processTicket(ticket: Ticket) { ... }
    ```

### Commit Messages
- Commit messages are **freeform** (no enforced prefix).
- Average commit message length: ~32 characters.
  - Example:
    ```
    Fix bug in ticket assignment logic
    ```

## Workflows

_No explicit workflows detected in the repository._

## Testing Patterns

- **Test files** use the pattern: `*.test.*`
  - Example:  
    ```
    ticket-handler.test.ts
    ```
- **Testing framework** is unknown; check test files for specifics.
- Place tests alongside the files they test or in a dedicated `tests/` directory.

#### Example Test File
```typescript
// ticket-handler.test.ts
import { processTicket } from './ticket-handler';

describe('processTicket', () => {
  it('should assign a ticket to a user', () => {
    // test implementation
  });
});
```

## Commands
| Command | Purpose |
|---------|---------|
| /test   | Run all test files matching `*.test.*` |
| /lint   | Lint the codebase for style issues     |
| /build  | Build the TypeScript project           |

```