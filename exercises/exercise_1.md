# Exercise 1: Baseline Implementation

## Overview

This is the first of three exercises in the AI Coding Summit workshop. Exercise 1 is designed to establish your personal baseline for AI-assisted coding **before** learning systematic techniques.

You'll implement product filtering capabilities in both the backend API and frontend interface of an e-commerce product catalog, working exactly as you would in a real project today.

**Important**: This is a baseline assessment, not a test. Use AI coding assistants however you're most comfortable. There are no rules, restrictions, or requirements on how you use AI tools - just work naturally.

## Goals

1. **Implement a complete fullstack feature** from backend to frontend
2. **Establish your baseline** for time, effort, and confidence when using AI assistants
3. **Experience your current workflow** before learning optimization techniques in Exercises 2 and 3

## The Task

You'll implement product filtering in two parts:

### Use AI However You Want

There are **no rules or restrictions** on AI usage:

- **Work exactly as you normally would if you got this task in a real project today**
- Use whatever prompting style feels natural to you
- Ask for help, code generation, debugging - whatever you need

### Part 1: Backend API Filtering

Add filtering capabilities to the FastAPI backend:

- **Price filtering**: Support minimum and maximum price filters
- **Category filtering**: Allow filtering by product category
- **Keyword search**: Search product names and descriptions
- **Sorting**: Enable sorting by price or name (both directions)

All filters should be optional and work together when combined.

### Part 2: Frontend Filtering UI

Build a React frontend interface that connects to your backend filtering API:

- **Price range controls**: Allow users to set min/max price filters
- **Category selector**: Enable filtering by product category
- **Search input**: Provide keyword search functionality
- **Sort controls**: Allow users to sort results
- **Filter management**: Ability to apply and clear filters

The interface should handle loading states, empty results, and validation errors appropriately.

## Project Structure

```
ai-coding-summit-workshop/
├── app/
│   ├── backend/      # FastAPI backend application
│   │   ├── app/
│   │   │   ├── api/
│   │   │   ├── models/
│   │   │   ├── services/
│   │   │   └── ...
│   │   └── tests/    # Backend tests (make these pass!)
│   └── frontend/     # React frontend application
│       └── src/
│           ├── components/
│           ├── lib/
│           └── types/
```

## Getting Started

### 1. Review the Codebase

Familiarize yourself with:

- **Backend**: `app/backend/app/` - Note the existing patterns for models, services, and logging
- **Frontend**: `app/frontend/src/` - Review the existing components and API client
- **Tests**: `app/backend/tests/` - Examine `test_products_filtering.py` to see what needs to pass

### 2. Start Backend Development

```bash
cd app/backend

# Install dependencies
uv venv --python 3.12
uv sync

# Start development server
uv run python run_api.py
```

Implement the backend filtering feature described above. Use AI assistants in whatever way feels natural to you.

### 3. Start Frontend Development

Once your backend filtering is working:

```bash
cd app/frontend

# Install dependencies
bun install

# Start development server
bun dev
```

Implement the frontend filtering UI described above. Again, use AI however you normally would.

## What to Track

As you work, please track the following metrics:

### ⏱️ Time Tracking

- **Backend time**: How long did TASK1 take?
- **Frontend time**: How long did TASK2 take?
- **Total time**: Overall exercise duration

### 💬 AI Interaction

- **Number of prompts**: How many times did you prompt your AI assistant?
- **Types of requests**: Were you asking for code generation? Debugging? Explanations?
- **Iteration cycles**: How many back-and-forth exchanges did it take?

### 😊 Confidence Level

After completing both tasks, rate your confidence (1-10):

- How confident are you that the code is **correct**?
- How confident are you that the code follows **best practices**?
- How well do you **understand** the generated code?
- How **maintainable** is the resulting code?

### 🐛 Issues Encountered

- Did the AI make mistakes? What kinds?
- Did you need to debug generated code?
- Were there type errors or test failures?
- How much manual fixing was required?

## Success Criteria

You've completed the exercise when:

- ✅ All backend tests pass (`uv run pytest`)
- ✅ Backend API accepts and processes filter parameters correctly
- ✅ Frontend displays a working filter interface
- ✅ Filters can be applied and results update accordingly
- ✅ You can manually test the full filtering flow in the browser

## Important Notes

### This is Not a Competition

The goal is to establish **your personal baseline**, not to compete with others. Be honest about:

- Time taken (don't rush!)
- Prompts used (track them all)
- Confidence levels (be realistic)
- Issues encountered (document everything)

### Documentation is Key

After completing the exercise, you'll reflect on:

- What worked well in your AI workflow?
- What was frustrating or slow?
- Where did you get stuck?
- What would you want to improve?

This reflection will inform the learning modules that follow.

## After Completion

When you're done, you'll have:

1. A working fullstack filtering feature
2. Baseline metrics for your AI-assisted coding workflow
3. Awareness of your current strengths and pain points
4. Context for the optimization techniques you'll learn next

## Questions?

- Check the main [README.md](./README.md) for project architecture and setup details
- Review existing code patterns in `app/backend/app/` and `app/frontend/src/`
- Run `/health` endpoint to verify backend is running: http://localhost:8000/health
- Check API docs when backend is running: http://localhost:8000/docs

## Ready?

Start implementing and use AI coding assistants however you normally would. Track your time, prompts, and confidence as you go.

Good luck!
