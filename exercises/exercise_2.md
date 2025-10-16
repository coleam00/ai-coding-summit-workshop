# Exercise 2: Systematic Implementation (PIV Loop)

## Overview

This is the second exercise in the AI Coding Summit workshop. After experiencing your natural workflow in Exercise 1, you'll now learn and apply the **PIV Loop** - a systematic approach to AI-assisted coding that dramatically improves output quality and gives you more control over the implementation.

**PIV Loop**: Planning → Implementing → Validating → Iterating

## Goals

1. **Experience systematic AI-assisted coding** using the PIV Loop methodology
2. **Compare the difference** in process smoothness and control versus Exercise 1
3. **Learn to create rich context** that guides AI toward better implementations
4. **Stay in the driver's seat** while delegating coding work to your AI assistant

## The PIV Loop Methodology

### 1. Planning

**Before writing any code**, create a comprehensive implementation plan that includes:

- **Success Criteria**: What does "done" look like? How will you validate it?
- **Documentation References**: What files, patterns, or conventions should be followed?
- **Task Breakdown**: What are the specific steps needed?
- **Desired Codebase Structure**: What files will be created/modified? What patterns should be used?

This plan becomes the **context** you provide to your AI assistant for every prompt.

### 2. Implementing

Execute your plan with AI assistance:

- Provide your full plan as context in your prompts
- Reference specific parts of the plan for each implementation step
- Keep the AI focused on your desired structure and patterns
- Maintain control over what gets implemented and how

### 3. Validating

Verify that the implementation matches your plan:

- Run automated tests
- Check that code follows the patterns you specified
- Verify that success criteria are met
- Look for deviations from your plan

### 4. Iterating

Refine based on validation results:

- Fix any issues found during validation
- Adjust the plan if needed based on what you learned
- Keep the AI aligned with your updated understanding
- Maintain the quality bar you set in your plan

## The Task

You'll implement the same product filtering feature from Exercise 1, but this time using the PIV Loop methodology.

### Part 1: Create Your Implementation Plan

Start with the structured task specifications provided:

- **Backend Task**: `tasks/TASK1.md`
- **Frontend Task**: `tasks/TASK2.md`

These tasks are written in the format you might receive from a project management tool like Linear, Jira, or Asana. They include:

- Requirements and acceptance criteria
- Technical notes and constraints
- Definition of done

Use these task specifications to create a detailed implementation plan that includes:

1. **Success Criteria**: How will you know you're done?
   - All tests in `app/backend/tests/test_products_filtering.py` pass
   - Frontend UI provides all required filtering controls
   - Manual testing checklist items pass

2. **Documentation to Reference**:
   - Existing code patterns in `app/backend/app/`
   - Existing frontend patterns in `app/frontend/src/`
   - Test files that show expected behavior

3. **Task Breakdown**:
   - Backend: Parameter model, service function, endpoint updates
   - Frontend: Filter component, API client updates, state management

4. **Desired Codebase Structure**:
   - What naming conventions to use
   - What file organization to follow
   - What logging patterns to implement
   - What type safety to maintain

### Part 2: Implement Using Your Plan

With your plan created, implement the features:

- Provide your full plan as context when prompting your AI assistant
- Reference specific sections of your plan for each step
- Keep your AI focused on your desired approach
- Notice how much more control you have compared to Exercise 1

### Part 3: Validate and Iterate

After implementation:

- Run the test suite: `cd app/backend && uv run pytest tests/ -v`
- Test the UI manually
- Check that code follows your planned patterns
- Iterate on any issues found

## What to Track

As you work through Exercise 2, track:

### Process Comparison

- **Planning Time**: How long did it take to create your plan?
- **Implementation Time**: How long to implement with the plan as context?
- **Validation Time**: How long to test and verify?
- **Total Time**: Compare to Exercise 1 total time

### Control and Understanding

- **How much more control** did you feel compared to Exercise 1?
- **How well did the AI follow** your plan and structure?
- **How much did you understand** what was being implemented?
- **How confident are you** in the resulting code quality?

### AI Interaction Quality

- **Number of prompts**: More or fewer than Exercise 1?
- **Prompt effectiveness**: Did the AI understand your intentions better?
- **Rework required**: How much code needed to be redone?

## Success Criteria

You've completed Exercise 2 when:

- ✅ You created a comprehensive implementation plan before coding
- ✅ All backend tests pass (`uv run pytest`)
- ✅ Frontend filtering UI works as specified
- ✅ Code follows your planned patterns and structure
- ✅ You can articulate how the PIV Loop improved your workflow

## Key Differences from Exercise 1

| Aspect | Exercise 1 | Exercise 2 |
|--------|-----------|-----------|
| **Approach** | Ad-hoc prompting | Planned, systematic |
| **Context** | Minimal | Rich, structured plan |
| **Control** | Following AI suggestions | Directing AI with plan |
| **Understanding** | Learning as you go | Understanding upfront |
| **Validation** | Reactive debugging | Proactive verification |

## Tips for Success

1. **Don't skip planning**: It feels like extra work, but it saves time overall
2. **Make your plan detailed**: The more specific, the better the AI can follow it
3. **Include examples**: Reference existing code patterns you want to emulate
4. **Use your plan as context**: Copy relevant sections into every prompt
5. **Validate frequently**: Don't wait until the end to check if things work
6. **Update your plan**: If you discover something new, adjust the plan

## After Exercise 2

Reflect on your experience:

- How much smoother was the process compared to Exercise 1?
- How much more control did you feel over the implementation?
- What parts of the planning phase were most valuable?
- How much more confident are you in the resulting code?
- What would you do differently next time?

## Ready?

1. Read the task specifications in `tasks/TASK1.md` and `tasks/TASK2.md`
2. Create your comprehensive implementation plan
3. Implement using the PIV Loop methodology
4. Compare your experience to Exercise 1

The difference should be dramatic. Good luck!
