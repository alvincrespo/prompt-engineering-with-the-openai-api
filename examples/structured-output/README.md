# Structured Output

## Purpose

This directory demonstrates how to generate various structured output formats using prompt engineering. Learning to control output format is crucial for integrating AI responses into applications and workflows.

## Subdirectories

### conditional/

Examples showing how to generate output based on conditions or criteria.

#### single.py

**Lesson:** Generate output that meets specific conditions.

**What you'll learn:**
- How to specify conditions in prompts
- Controlling output based on criteria
- Conditional formatting patterns

**Run from root:**
```bash
python examples/structured-output/conditional/single.py
```

---

#### multiple.py

**Lesson:** Handle multiple conditions in output generation.

**What you'll learn:**
- Managing complex conditional logic
- Multiple criteria in a single prompt
- Nested or compound conditions

**Run from root:**
```bash
python examples/structured-output/conditional/multiple.py
```

**Key takeaway:** Break down complex conditions into clear, explicit statements for better results.

---

### lists/

Examples demonstrating list generation in different formats.

#### ordered.py

**Lesson:** Generate numbered or ordered lists.

**What you'll learn:**
- How to request ordered lists
- Using "ONLY" to prevent extra content
- Clean, minimal list formatting

**Run from root:**
```bash
python examples/structured-output/lists/ordered.py
```

**Key takeaway:** Be explicit about format. Words like "ONLY" help prevent unwanted explanations or context.

---

#### unordered.py

**Lesson:** Generate bulleted or unordered lists.

**What you'll learn:**
- Requesting unordered list formats
- Bullet point formatting
- Consistent list structure

**Run from root:**
```bash
python examples/structured-output/lists/unordered.py
```

---

### Root Level Files

#### tables.py

**Lesson:** Generate data in table format with columns and rows.

**What you'll learn:**
- How to specify table structure
- Defining column headers
- Getting markdown-formatted tables
- Requesting specific number of rows

**Run from root:**
```bash
python examples/structured-output/tables.py
```

**Key takeaway:** Clearly specify column names and the number of rows. The model defaults to markdown table format.

---

#### paragraphs.py

**Lesson:** Generate well-structured paragraphs with headings and subheadings.

**What you'll learn:**
- Requesting hierarchical content structure
- Getting markdown-formatted text with headers
- Organizing information logically
- Creating document-like outputs

**Run from root:**
```bash
python examples/structured-output/paragraphs.py
```

**Key takeaway:** Ask for "structured paragraphs with headings" to get well-organized, document-style output.

---

#### custom-output.py

**Lesson:** Define and receive custom output formats.

**What you'll learn:**
- Creating custom structure specifications
- Mixing different format elements
- Template-based output patterns
- Complex nested structures

**Run from root:**
```bash
python examples/structured-output/custom-output.py
```

**Key takeaway:** You can define almost any output structure. Provide examples or detailed specifications for best results.

## Best Practices

- **Be explicit about format** - State exactly what structure you want (table, list, JSON, etc.)
- **Specify constraints** - Use words like "ONLY", "exactly", or "no more than" to control output
- **Define column/field names** - For tables and structured data, list what fields you need
- **Use examples** - Show the model what your ideal output looks like
- **Request markdown formatting** - The model is excellent at markdown tables, headers, and lists
- **Iterate** - Start simple and add constraints if the output includes unwanted elements
