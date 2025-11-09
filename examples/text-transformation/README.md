# Text Transformation

## Purpose

This directory demonstrates various text transformation techniques using AI, including grammar correction, tone adjustment, translation, and multi-step transformations. These patterns are essential for content editing, localization, and communication optimization.

## Subdirectories

### adjustments/

Examples showing how to modify the tone and style of text.

#### generic.py

**Lesson:** Transform text from informal to formal tone.

**What you'll learn:**
- How to specify desired tone (formal, casual, professional, friendly)
- Maintaining message meaning while changing style
- Tone transformation for different audiences
- Creating contextually appropriate communication

**Run from root:**
```bash
python examples/text-transformation/adjustments/generic.py
```

**Key takeaway:** Specify both the current tone and desired tone for best results. The model can adapt text for different professional contexts.

---

#### targeted.py

**Lesson:** Adjust tone for specific target audiences.

**What you'll learn:**
- Writing for specific demographics or audiences
- Adapting language complexity
- Audience-aware communication
- Context-sensitive transformations

**Run from root:**
```bash
python examples/text-transformation/adjustments/targeted.py
```

**Key takeaway:** Explicitly mention your target audience (executives, children, technical experts, etc.) to get appropriately tailored content.

---

### languages/

Examples demonstrating translation and multilingual capabilities.

#### multi.py

**Lesson:** Translate text into multiple languages simultaneously.

**What you'll learn:**
- Multi-language translation in a single request
- Formatted output for multiple translations
- Maintaining consistency across languages
- Efficient batch translation

**Run from root:**
```bash
python examples/text-transformation/languages/multi.py
```

**Key takeaway:** You can request multiple translations at once. The model handles context and nuance well for major languages.

---

### Root Level Files

#### grammar.py

**Lesson:** Correct grammar and spelling while preserving structure and meaning.

**What you'll learn:**
- Proofreading and error correction
- Maintaining original text structure
- Fixing spelling and grammatical errors
- Preserving intent while improving clarity

**Run from root:**
```bash
python examples/text-transformation/grammar.py
```

**Key takeaway:** Use "keeping the original structure intact" to prevent the model from rewriting more than necessary. Focus changes on errors only.

---

#### multi-step.py

**Lesson:** Apply multiple transformations in sequence.

**What you'll learn:**
- Chaining multiple transformation steps
- Grammar correction + tone adjustment
- Translation + formatting
- Complex multi-stage text processing

**Run from root:**
```bash
python examples/text-transformation/multi-step.py
```

**Key takeaway:** You can request multiple transformations in a single prompt. List them clearly in order of application.

## Common Use Cases

- **Content Localization** - Translate marketing materials or documentation
- **Email Optimization** - Adjust tone for different recipients
- **Quality Assurance** - Proofread and correct written content
- **Audience Adaptation** - Rewrite content for different reader levels
- **Style Consistency** - Standardize tone across documents
- **Communication Polish** - Improve clarity and professionalism

## Best Practices

- **Use clear delimiters** - Triple backticks to separate the text to transform
- **Specify what to preserve** - "Keep the original structure", "maintain meaning", etc.
- **Be explicit about changes** - State exactly what should be transformed and what shouldn't
- **Request specific tones** - Use descriptive words: formal, casual, persuasive, empathetic, technical
- **Define your audience** - Who will read the transformed text?
- **Test with edge cases** - Very informal text, technical jargon, mixed languages
- **For translations** - Specify if you want literal or contextual translation
- **Multi-step order matters** - Apply grammar fixes before tone changes for best results

## Transformation Combinations

You can combine transformations effectively:
- **Grammar + Tone**: "Fix errors AND make it more professional"
- **Translation + Simplification**: "Translate to Spanish AND use simple vocabulary"
- **Tone + Length**: "Make it formal AND more concise"
- **Grammar + Structure**: "Fix errors AND organize into bullet points"
