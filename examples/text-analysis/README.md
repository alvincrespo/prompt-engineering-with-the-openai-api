# Text Analysis

## Purpose

This directory contains examples of using AI for text analysis tasks, including sentiment classification, categorization, and entity extraction. These patterns are fundamental for building text processing pipelines and content analysis tools.

## Subdirectories

### categories/

Examples demonstrating text categorization and sentiment analysis.

#### specified.py

**Lesson:** Classify text into predefined categories.

**What you'll learn:**
- How to specify allowed categories
- Getting single-word classification responses
- Sentiment analysis with constrained outputs
- Using clear delimiters for text separation

**Run from root:**
```bash
python examples/text-analysis/categories/specified.py
```

**Key takeaway:** When you want a specific set of categories, list them explicitly and request "a single word" answer to avoid explanations.

---

#### unspecified.py

**Lesson:** Let the model determine appropriate categories.

**What you'll learn:**
- Open-ended categorization
- When to let the model choose categories
- Discovering emergent patterns in text
- Flexible classification approaches

**Run from root:**
```bash
python examples/text-analysis/categories/unspecified.py
```

**Key takeaway:** For exploratory analysis, let the model suggest categories. This can reveal patterns you hadn't considered.

---

#### multiple.py

**Lesson:** Classify text into multiple categories simultaneously.

**What you'll learn:**
- Multi-label classification
- Handling texts that fit multiple categories
- Structured output for multiple classifications
- When to use multi-category vs single-category classification

**Run from root:**
```bash
python examples/text-analysis/categories/multiple.py
```

**Key takeaway:** Text often belongs to multiple categories. Explicitly state if you want single or multiple classifications.

---

### entity-extraction/

Examples showing how to extract specific information from text.

#### specific.py

**Lesson:** Extract predefined entities from text.

**What you'll learn:**
- How to specify which entities to extract
- Using bullet points to list desired entities
- Formatting extracted data
- Handling missing entities gracefully

**Run from root:**
```bash
python examples/text-analysis/entity-extraction/specific.py
```

**Key takeaway:** List the exact entities you want to extract. This works well for structured data extraction from product descriptions, articles, or documents.

---

#### few-shot.py

**Lesson:** Use examples to guide entity extraction patterns.

**What you'll learn:**
- Providing examples of extraction format
- Consistency in entity naming
- Pattern recognition for complex extractions
- Handling variations in text structure

**Run from root:**
```bash
python examples/text-analysis/entity-extraction/few-shot.py
```

**Key takeaway:** Examples are especially helpful for entity extraction when the format or entity types might be ambiguous.

## Common Use Cases

- **Sentiment Analysis** - Determine if customer feedback is positive, negative, or neutral
- **Content Classification** - Categorize articles, emails, or support tickets
- **Data Extraction** - Pull structured information from unstructured text
- **Named Entity Recognition** - Identify people, places, organizations, products, etc.
- **Topic Detection** - Determine what subjects are discussed in text

## Best Practices

- **Use delimiters** - Triple backticks or other clear markers to separate the text being analyzed
- **Specify output format** - "single word", "bullet list", "JSON", etc.
- **List valid categories** - When you have predefined categories, list them explicitly
- **Be specific about entities** - List exactly which entities you want extracted
- **Request confidence levels** - If needed, ask "how confident are you?" for uncertain classifications
- **Handle edge cases** - Consider what should happen if no entities are found or text is ambiguous
- **Use few-shot for complex patterns** - Provide examples when the extraction pattern is not straightforward
