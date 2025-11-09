# Message Roles

## Purpose

This directory demonstrates how to use different message roles (system, user, assistant) in OpenAI's chat completion API. Understanding message roles is crucial for building conversational AI applications and providing context to the model.

## Examples

### script.py

**Lesson:** Use system messages to set the assistant's behavior and personality.

**What you'll learn:**
- The difference between system, user, and assistant roles
- How to use system messages to define the assistant's persona
- How to structure multi-role conversations
- The impact of role-based context on response quality

**Run from root:**
```bash
python examples/message-roles/script.py
```

**Key takeaway:** System messages are powerful tools for setting the tone, expertise level, and behavior of the AI assistant. Use them to create specialized assistants for specific domains or tasks.

## References

### OpenAI Documentation
- [Chat Completions API Guide](https://platform.openai.com/docs/guides/text-generation/chat-completions-api) - Official documentation on message roles
- [Building a Conversational AI](https://platform.openai.com/docs/guides/text) - Creating chat-based applications

### Tutorials and Examples
- [OpenAI Cookbook: Chat Examples](https://cookbook.openai.com/examples/how_to_format_inputs_to_chatgpt_models) - Formatting messages for chat models
- [Role-Based Prompting Guide](https://www.promptingguide.ai/guides/context-engineering-guide.en#context-engineering-in-action) - Using personas and roles in prompts
