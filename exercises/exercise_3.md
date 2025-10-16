# Exercise 3: Reusable Prompts Only

## Overview

This is the third and final exercise in the AI Coding Summit workshop. After learning the PIV Loop in Exercise 2, you'll now master the ultimate level of systematic AI-assisted coding: **using only reusable prompts** (also known as slash commands or /commands).

In this exercise, you're **not allowed** to type directly into your AI assistant's chat except to invoke a command. All interactions must go through pre-defined reusable prompts. This constraint forces you to think systematically and helps you build a library of reliable, repeatable workflows.

## Goals

1. **Master reusable prompts** for consistent, efficient AI-assisted coding
2. **Build systematic workflows** that can be reused across projects
3. **Enforce best practices** through structured prompts
4. **Experience ultimate control** over AI interactions

## What Are Reusable Prompts?

Reusable prompts (also called slash commands or /commands) are pre-written prompts that:

- Embed consistent context and instructions
- Enforce best practices and patterns
- Can be invoked with a simple command
- Provide repeatable, reliable results

**Example**: Instead of typing "please implement a filter function for products", you invoke a command like `/implement` that includes comprehensive context about your codebase patterns, logging requirements, type safety standards, etc.

## The Challenge: Commands Only

For this exercise, you must:

- ✅ Use ONLY the commands in `rules-and-commands/commands/`
- ✅ Leverage the global rules in `rules-and-commands/rules/`
- ✅ Edit existing commands or create new ones as needed
- ❌ NO typing directly into the AI chat
- ❌ NO ad-hoc prompts

This constraint might feel limiting at first, but it teaches you to:

- Think about what reusable patterns you need
- Build a library of effective prompts
- Achieve consistency across all implementations

## Available Resources

### Global Rules (`rules-and-commands/rules/`)

Global rules are automatically included in every AI interaction. They set the baseline standards for:

- Code quality and style
- Naming conventions
- Logging patterns
- Type safety requirements
- Testing practices

Review these rules to understand the baseline context your AI assistant always has.

### Commands (`rules-and-commands/commands/`)

Commands are reusable prompts you can invoke. Explore the existing commands to see what's available. Common command patterns might include:

- `/plan` - Create an implementation plan
- `/implement` - Implement a feature following patterns
- `/test` - Run tests and fix issues
- `/review` - Review code quality
- `/debug` - Debug a specific issue

**Note**: The actual commands available depend on what's in your `rules-and-commands/commands/` folder. Review that folder to see what's provided.

## The Task

Implement a new feature or enhancement to the product catalog application using ONLY reusable prompts.

### Part 1: Understand Your Tools

Before starting:

1. **Review Global Rules**: Read all files in `rules-and-commands/rules/`
   - What standards are automatically enforced?
   - What context is always provided?

2. **Review Available Commands**: Read all files in `rules-and-commands/commands/`
   - What commands exist?
   - What does each command do?
   - What parameters do they accept?

3. **Identify Gaps**: What commands might you need that don't exist?

### Part 2: Plan Your Command Strategy

Think about your implementation workflow:

- What command will you use for planning?
- What command will you use for implementation?
- What command will you use for validation?
- Do you need to create or edit any commands?

### Part 3: Implement Using Commands Only

Execute your implementation:

- Invoke commands for each step of your workflow
- Edit commands if they don't quite fit your needs
- Create new commands if you discover missing patterns
- **Never type directly into the chat** - only use commands

### Part 4: Reflect on Command Effectiveness

After implementation:

- Which commands were most valuable?
- Which commands needed editing?
- What new commands did you create?
- How reusable are your commands for future projects?

## What to Track

As you work through Exercise 3, track:

### Workflow Metrics

- **Commands Used**: Which commands did you invoke?
- **Commands Created**: What new commands did you add?
- **Commands Edited**: What existing commands did you modify?
- **Time to Completion**: How long compared to Exercises 1 and 2?

### Quality and Control

- **Consistency**: How consistent was the AI output?
- **Control**: How much control did you have over the implementation?
- **Understanding**: How well do you understand the patterns?
- **Reusability**: How reusable are your commands for future work?

### Comparison to Previous Exercises

| Metric | Exercise 1 | Exercise 2 | Exercise 3 |
|--------|-----------|-----------|-----------|
| **Approach** | Ad-hoc | Planned | Systematic |
| **Context** | Minimal | Rich plan | Embedded rules |
| **Consistency** | Variable | Better | Excellent |
| **Reusability** | None | Some | High |
| **Control** | Low | Medium | High |

## Success Criteria

You've completed Exercise 3 when:

- ✅ Feature implemented using ONLY reusable prompts (no direct chat)
- ✅ All tests pass and feature works as expected
- ✅ Code follows all global rules and patterns
- ✅ You have a library of commands you could reuse on future projects
- ✅ You understand the power of systematic, reusable workflows

## Tips for Success

### 1. Start with Planning Commands

Use a command to create your plan, don't try to plan in your head.

### 2. Edit Commands Liberally

If a command doesn't quite fit, edit it! Commands should evolve to match your needs.

### 3. Create Commands for Common Patterns

If you find yourself wanting to do something repeatedly, create a command for it.

### 4. Keep Commands Focused

Each command should do one thing well. Don't try to make a command that does everything.

### 5. Include Rich Context in Commands

Commands should embed all the context the AI needs:
- References to documentation
- Examples of patterns to follow
- Success criteria
- Validation steps

### 6. Test Your Commands

After creating or editing a command, test it to make sure it produces the results you want.

## Example Command Structure

Here's what a good command might look like:

```markdown
# /implement

You are implementing a feature in the product catalog application.

**Context**:
- Review existing patterns in app/backend/app/ and app/frontend/src/
- Follow the service layer architecture
- Use comprehensive type hints
- Implement structured JSON logging
- Write tests alongside implementation

**Task**: [User will provide task description]

**Process**:
1. Review task requirements
2. Check existing code patterns
3. Implement following established patterns
4. Add structured logging
5. Update/create tests
6. Validate implementation

**Success Criteria**:
- All tests pass
- Code follows existing patterns
- Logging is comprehensive
- Types are complete
```

## After Exercise 3

Reflect on the three exercises:

### Exercise 1: Baseline
- How did it feel to work without structure?
- What challenges did you face?
- How much control did you have?

### Exercise 2: PIV Loop
- How did planning change the experience?
- How much more control did structured prompting give you?
- What was the quality difference?

### Exercise 3: Reusable Prompts
- How did commands enforce consistency?
- How reusable is your command library?
- What commands will you use in your daily work?

## Building Your Command Library

After completing this workshop, continue building your command library:

1. **Create commands for your common tasks**:
   - Feature implementation
   - Bug fixing
   - Code review
   - Refactoring
   - Documentation

2. **Embed your team's standards**:
   - Coding conventions
   - Architecture patterns
   - Testing requirements
   - Documentation format

3. **Share with your team**:
   - Consistent prompts = consistent code
   - Team members can use the same commands
   - Onboarding becomes easier

4. **Iterate and improve**:
   - Commands should evolve with your needs
   - Update them based on what works
   - Remove or consolidate commands that don't add value

## Ready?

1. Review the global rules in `rules-and-commands/rules/`
2. Explore available commands in `rules-and-commands/commands/`
3. Plan which commands you'll use (using a command, of course!)
4. Implement using ONLY reusable prompts
5. Reflect on how systematic AI-assisted coding has transformed your workflow

Remember: You cannot type directly into the chat. All interactions must be through commands. This constraint is the key to building systematic, reusable workflows.

Good luck with your final exercise!
