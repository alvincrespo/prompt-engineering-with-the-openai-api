# Code Generation

## Purpose

This directory contains examples of using prompt engineering for code-related tasks, including code explanation, modification, and generation from specifications. These patterns are essential for building AI-powered development tools.

## Subdirectories

### explanation/

Examples demonstrating how to get the model to explain existing code.

#### generic.py

**Lesson:** Get concise, high-level explanations of code functionality.

**What you'll learn:**
- How to request brief code summaries
- Using delimiters (triple backticks) to clearly separate code from instructions
- Getting focused, single-sentence explanations

**Run from root:**
```bash
python examples/code-generation/explanation/generic.py
```

**Key takeaway:** Be explicit about the level of detail you want. A one-sentence summary is useful for quick understanding.

---

#### detailed.py

**Lesson:** Get comprehensive, step-by-step code explanations.

**What you'll learn:**
- Using "Let's think step by step" for detailed analysis
- Getting line-by-line breakdowns of code logic
- Understanding potential edge cases and assumptions

**Run from root:**
```bash
python examples/code-generation/explanation/detailed.py
```

**Key takeaway:** The phrase "Let's think step by step" encourages the model to provide thorough, methodical explanations.

---

### modification/

Examples showing how to modify or transform existing code.

#### no-step.py

**Lesson:** Make targeted modifications to existing code.

**What you'll learn:**
- How to request specific code changes
- Maintaining code context during modifications
- Getting both the modified code and explanations

**Run from root:**
```bash
python examples/code-generation/modification/no-step.py
```

---

#### multi-step.py

**Lesson:** Apply multiple transformations to code in sequence.

**What you'll learn:**
- How to chain multiple code modifications
- Maintaining coherence across multiple changes
- Complex refactoring patterns

**Run from root:**
```bash
python examples/code-generation/modification/multi-step.py
```

**Key takeaway:** Break complex code changes into clear, sequential steps for better results.

---

### Root Level Files

#### input-output.py

**Lesson:** Generate code from input-output examples.

**What you'll learn:**
- How to specify behavior through examples
- Inferring program logic from test cases
- The power of example-driven development

**Run from root:**
```bash
python examples/code-generation/input-output.py
```

**Key takeaway:** Providing input-output examples is an effective way to communicate program requirements without writing explicit specifications.

---

#### prompts.py

**Lesson:** Collection of various code generation prompt patterns.

**What you'll learn:**
- Different approaches to code generation prompts
- Various ways to structure code requests
- Prompt templates for common coding tasks

**Run from root:**
```bash
python examples/code-generation/prompts.py
```

## Best Practices

- **Use clear delimiters** (e.g., triple backticks) to separate code from instructions
- **Be specific about output format** - Do you want just code, code with comments, or code with explanations?
- **Provide context** - Include relevant information about the programming language, frameworks, or constraints
- **Use examples** - Input-output examples are often clearer than lengthy descriptions
- **Request step-by-step thinking** - For complex tasks, ask the model to "think step by step"
