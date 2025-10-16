# AI Coding Summit Workshop

A hands-on workshop that demonstrates the dramatic difference between fumbling and systematic AI-assisted coding. This project contains a full-stack e-commerce product catalog application designed as a training ground for learning effective AI coding techniques.

**Prerequisites**: If you need to install any prerequisites (Python, Node, Git, an AI coding assistant), see the [SETUP_GUIDE.md](./SETUP_GUIDE.md).

## Quick Start

Get the application running in two terminals:

**Terminal 1 - Backend**:
```bash
cd app/backend
uv venv --python 3.12
uv sync
uv run python run_api.py
# → http://localhost:8000
```

**Terminal 2 - Frontend**:
```bash
cd app/frontend
bun install
bun dev
# → http://localhost:3000
```

## Project Overview

This workshop challenges participants to implement product filtering capabilities in a full-stack application (FastAPI backend + React frontend). The same feature will be implemented multiple times using progressively more sophisticated approaches to AI-assisted coding.

## The Three Exercises

### Exercise 1: Baseline Implementation

**Goal**: Establish your personal baseline for AI-assisted coding without structured techniques.

In this first exercise, you'll implement product filtering features in both the backend and frontend exactly as you would in a normal project today. Use AI coding assistants however you're most comfortable - there are no rules or restrictions.

**Important Note**: Your implementation will likely work, even with simple prompts - AI coding assistants are powerful enough to handle these features. This project is intentionally straightforward because **the goal isn't to struggle with getting code to work**. Instead, pay attention to:
- How smooth does the process feel?
- How much do you understand what's being implemented?
- How much control do you feel you have over the specific implementation details?
- Are you in the driver's seat, or just along for the ride?

This workshop is about learning to stay in the driver's seat while delegating the coding work to your AI assistant.

**What You'll Do**:
- Add filtering capabilities to the FastAPI backend (price, category, keyword search, sorting)
- Build a React filtering interface that connects to your backend API
- Get all tests passing and verify the feature works end-to-end

**What to Track**:
- Time spent on backend and frontend
- Number of AI prompts and iterations
- How much control you felt over the implementation details
- How well you understand what was implemented
- Issues encountered and debugging time

**See [exercises/exercise_1.md](./exercises/exercise_1.md) for complete Exercise 1 instructions.**

### Exercise 2: Systematic Implementation (PIV Loop)

**Goal**: Experience the power of systematic planning and structured AI prompting.

After learning about the PIV Loop (Planning → Implementing → Validating → Iterating), you'll implement a new feature using a structured approach. This exercise demonstrates how upfront planning and rich context dramatically improves AI output quality and gives you more control over the implementation.

**The PIV Loop Approach**:
1. **Planning**: Create a detailed implementation plan with:
   - Clear success criteria
   - Documentation references
   - Task breakdown
   - Desired codebase structure
2. **Implementing**: Execute the plan with AI assistance
3. **Validating**: Run tests and verify functionality
4. **Iterating**: Refine based on validation results

**What You'll Do**:
- Start with the structured task specifications in `tasks/TASK1.md` and `tasks/TASK2.md`
- Create a comprehensive implementation plan before writing code
- Use the plan as context for all AI prompts
- Track how much smoother the process feels compared to Exercise 1 and the level of control you have

**See [exercises/exercise_2.md](./exercises/exercise_2.md) for complete Exercise 2 instructions.**

### Exercise 3: Reusable Prompts Only

**Goal**: Master the use of global rules and reusable prompts for consistent, efficient AI coding.

After learning about global rules and slash commands (reusable prompts), you'll implement features using ONLY pre-defined reusable prompts. This constraint forces you to leverage systematic patterns so you can learn to build your own reliable and reusable workflows for using AI coding assistants.

**The Challenge**:
- Implement features using ONLY the commands in `rules-and-commands/commands/`
- Leverage the global rules in `rules-and-commands/rules/`
- You can edit existing commands or create new ones, but all AI interactions must go through reusable prompts
- NO typing directly into the AI chat except to invoke commands

**What You'll Learn**:
- How reusable prompts enforce best practices
- The power of consistent context across all AI interactions
- How to build a library of effective prompts for your workflow

**See [exercises/exercise_3.md](./exercises/exercise_3.md) for complete Exercise 3 instructions.**

## Project Architecture

### Backend (FastAPI + Python 3.12)

**Location**: `app/backend/`

**Tech Stack**:
- FastAPI for REST API
- Pydantic for data validation
- Structured JSON logging
- pytest for testing
- Ruff for code quality

**Key Features**:
- Service layer architecture (clear separation of concerns)
- Comprehensive type hints on all functions
- Verbose, AI-friendly naming (`product_price_usd`, `filter_products_by_category_and_price_range`)
- Structured JSON logging to stdout for AI debugging
- Complete docstrings with examples
- 30 sample products across 5 categories

**Quick Start**:
```bash
cd app/backend
uv venv --python 3.12
uv sync
uv run python run_api.py
```

**Testing**:
```bash
uv run pytest tests/ -v
```

### Frontend (React 19 + TypeScript)

**Location**: `app/frontend/`

**Tech Stack**:
- Bun runtime
- React 19 with TypeScript
- shadcn/ui components (New York theme)
- Tailwind CSS v4
- Biome for linting and formatting
- React Hook Form + Zod validation

**Key Features**:
- Types match backend Pydantic models EXACTLY
- Structured JSON logging (mirrors backend pattern)
- Type-safe API client
- Proper loading, error, and empty states
- Accessibility-first component patterns
- Hot module reloading for fast development

**Quick Start**:
```bash
cd app/frontend
bun install
bun dev  # → http://localhost:3000
```

**Code Quality**:
```bash
bun run check     # Lint and format check
bun run check:fix # Auto-fix issues
```

## Development Workflow

1. **Start Backend** (Terminal 1):
   ```bash
   cd app/backend
   uv run python run_api.py
   # → http://localhost:8000
   ```

2. **Start Frontend** (Terminal 2):
   ```bash
   cd app/frontend
   bun dev
   # → http://localhost:3000
   ```

3. **Run Tests** (Terminal 3):
   ```bash
   cd app/backend
   uv run pytest tests/ -v
   ```

## Key Learning Principles

### 1. AI-Friendly Code Patterns

Both backend and frontend demonstrate patterns that work exceptionally well with AI:

- **Verbose naming**: `product_price_usd` instead of `price`
- **Complete type hints**: Every function fully typed
- **Structured logging**: JSON logs for AI debugging
- **Comprehensive docs**: Docstrings with examples everywhere
- **Clear patterns**: Consistent architecture makes AI suggestions more accurate

### 2. Context Engineering

The exercises progressively demonstrate how rich context improves AI output:

- **Exercise 1**: Minimal context → lots of iteration and debugging
- **Exercise 2**: Rich planning context → smooth implementation
- **Exercise 3**: Reusable prompts with embedded context → consistent excellence

### 3. Validation-First Development

Tests are provided upfront to validate your implementation:

- Backend: `app/backend/tests/test_products_filtering.py`
- Clear acceptance criteria in task specifications
- Fast feedback loops with automated tests

## Resources

- **Exercise 1 Instructions**: [exercises/exercise_1.md](./exercises/exercise_1.md)
- **Exercise 2 Instructions**: [exercises/exercise_2.md](./exercises/exercise_2.md)
- **Exercise 3 Instructions**: [exercises/exercise_3.md](./exercises/exercise_3.md)
- **Setup Guide**: [SETUP_GUIDE.md](./SETUP_GUIDE.md)
- **Task Specifications**: `tasks/TASK1.md` and `tasks/TASK2.md`
- **Reusable Prompts**: `rules-and-commands/commands/`
- **Global Rules**: `rules-and-commands/rules/`

## Success Metrics

Track your progress across all three exercises:

- **Time to completion**: How long does each approach take?
- **AI prompt efficiency**: How many prompts needed?
- **Code confidence**: How confident are you in the result?
- **Debugging effort**: How much manual fixing was required?
- **Learning insights**: What did you discover about effective AI prompting?

## Getting Help

- **API docs**: http://localhost:8000/docs (when backend is running)
- **Health check**: http://localhost:8000/health
- **Type definitions**: `app/backend/app/models/` and `app/frontend/src/types/`
- **Example patterns**: Review existing code in both backend and frontend

## Ready to Start?

Begin with **[exercises/exercise_one.md](./exercises/exercise_one.md)** for Exercise 1. Remember: the goal is to establish your personal baseline first, then experience the dramatic improvement that systematic AI-assisted coding provides.

Good luck!
