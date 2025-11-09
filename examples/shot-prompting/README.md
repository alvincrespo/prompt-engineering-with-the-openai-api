# Shot Prompting

## Purpose

This directory demonstrates different shot prompting techniques: zero-shot, one-shot, and few-shot learning. These techniques control how many examples you provide to the model to guide its behavior and output format.

## Examples

### zero-shot.py

**Lesson:** Get accurate responses without providing any examples.

**What you'll learn:**
- How to structure zero-shot prompts
- When zero-shot prompting is appropriate
- The model's capability to understand tasks without examples

**Run from root:**
```bash
python examples/shot-prompting/zero-shot.py
```

**Key takeaway:** Modern language models can handle many tasks without examples. Start with zero-shot and add examples only if needed.

---

### one-shot.py

**Lesson:** Provide a single example to demonstrate the desired output format or pattern.

**What you'll learn:**
- How one example can guide the model's output
- When one example is sufficient
- Pattern recognition from single examples

**Run from root:**
```bash
python examples/shot-prompting/one-shot.py
```

**Key takeaway:** A single well-chosen example can be enough to establish a clear pattern for the model to follow.

---

### few-shot.py

**Lesson:** Use multiple examples to establish clear patterns and improve accuracy.

**What you'll learn:**
- How to structure few-shot prompts with multiple examples
- The balance between number of examples and token usage
- Pattern recognition and consistency

**Run from root:**
```bash
python examples/shot-prompting/few-shot.py
```

**Key takeaway:** Multiple examples help the model understand nuanced patterns, especially for classification or structured tasks.

---

### few-shot-assistant.py

**Lesson:** Use assistant role messages to provide examples in a conversational format.

**What you'll learn:**
- How to structure few-shot examples using message roles
- The difference between inline examples and role-based examples
- Building conversational patterns

**Run from root:**
```bash
python examples/shot-prompting/few-shot-assistant.py
```

**Key takeaway:** Using assistant role for examples creates more natural conversational patterns and can improve context understanding.

## General Guidelines

- **Start with zero-shot** - Only add examples if the output isn't meeting your needs
- **Use one-shot for simple patterns** - Often sufficient for format guidance
- **Use few-shot for complex tasks** - Classification, nuanced formatting, or domain-specific outputs
- **Quality over quantity** - 3-5 well-chosen examples are usually better than many mediocre ones

## References

### Research Papers
- [Language Models are Few-Shot Learners (GPT-3)](https://arxiv.org/abs/2005.14165) - Foundational paper introducing few-shot learning with language models
- [Chain-of-Thought Prompting](https://arxiv.org/abs/2201.11903) - Enhanced reasoning through step-by-step examples
- [In-Context Learning Survey](https://arxiv.org/abs/2301.00234) - Comprehensive survey of in-context learning techniques

### Guides and Tutorials
- [OpenAI Guide: Few-Shot Learning](https://platform.openai.com/docs/guides/prompt-engineering/tactic-provide-examples) - Official documentation on providing examples
- [Prompt Engineering Guide: Few-Shot Prompting](https://www.promptingguide.ai/techniques/fewshot) - Detailed techniques and best practices
- [Few-Shot Prompting Examples](https://learnprompting.org/docs/basics/few_shot) - Practical examples and use cases
