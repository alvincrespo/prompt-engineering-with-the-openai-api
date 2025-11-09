# Get Response Usage

## Purpose

This directory contains examples demonstrating how to use the shared `get_response` helper function from `utils.openai_client`. These examples show the simplest way to interact with the OpenAI API using the repository's standardized approach.

## Examples

### import-example.py

**Lesson:** Use the centralized helper function for consistent API calls.

**What you'll learn:**
- How to import and use the `get_response` helper
- The advantage of centralized API configuration
- Keeping scripts clean and focused on prompts
- Avoiding repetitive boilerplate code

**Run from root:**
```bash
python examples/get-response/import-example.py
```

**Key takeaway:** Using the `get_response` helper from `utils.openai_client` centralizes your OpenAI configuration, making scripts cleaner and easier to maintain. All examples in this repository follow this pattern.

## Why Use the Helper Function?

### Benefits

1. **Consistency** - All scripts use the same model and settings
2. **Maintainability** - Change API configuration in one place
3. **Simplicity** - Less boilerplate in each example script
4. **Environment Variables** - Automatic `.env` file loading
5. **Type Safety** - Supports both string prompts and message arrays

### The Helper Function

Located in `utils/openai_client.py`, the helper provides:

```python
def get_response(input: Union[str, list[dict]]) -> str:
    """
    Accepts either:
    - A simple string prompt
    - A list of message dictionaries with roles
    
    Returns the model's response as a string
    """
```

### Two Ways to Use It

**Simple string prompt:**
```python
from utils.openai_client import get_response

response = get_response("Your prompt here")
print(response)
```

**Message array with roles:**
```python
from utils.openai_client import get_response

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]
response = get_response(messages)
print(response)
```

## Configuration

The helper uses these default settings:
- **Model**: `gpt-4o-mini`
- **Temperature**: `0` (deterministic)
- **Environment**: Loads from `.env` file

To use different settings, you can modify `utils/openai_client.py` once, and all examples will inherit the changes.
