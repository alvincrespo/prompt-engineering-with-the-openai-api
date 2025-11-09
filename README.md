# Prompt Engineering with the OpenAI API

A collection of self-contained Python scripts demonstrating prompt engineering patterns and best practices using the OpenAI API.

## Purpose

This repository hosts small, practical examples that show how to effectively use prompt engineering techniques with OpenAI's models. Each topic lives in its own folder with a single runnable script, making it easy to explore specific patterns without complex setup.

## Repository Structure

```
prompt-engineering-with-the-openai-api/
├── introduction-to-prompt-engineering-best-practices/
│   └── introduction-to-prompt-engineering.py
├── requirements.txt
├── .env.example
└── README.md
```

Each example follows a consistent pattern:
- One folder per topic
- One runnable `.py` file per folder
- Minimal dependencies
- Clear, inspectable output to stdout

## Prerequisites

- Python 3.10 or higher
- An OpenAI API key ([get one here](https://platform.openai.com/api-keys))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/prompt-engineering-with-the-openai-api.git
   cd prompt-engineering-with-the-openai-api
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your OpenAI API key:**

   Create a `.env` file in the project root:
   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

   Alternatively, export it directly:
   ```bash
   export OPENAI_API_KEY=sk-your-key-here
   ```

## Running the Examples

Each script is self-contained and can be run directly:

```bash
python introduction-to-prompt-engineering-best-practices/introduction-to-prompt-engineering.py
```

All examples use:
- **Model:** `gpt-4o` (unless specified otherwise)
- **Temperature:** `0` (deterministic responses)

## Code Pattern

All examples follow a consistent pattern for easy understanding:

```python
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def get_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content

# Example usage
response = get_response("Your prompt here")
print(response)
```

## Examples

### Introduction to Prompt Engineering
**Location:** `introduction-to-prompt-engineering-best-practices/introduction-to-prompt-engineering.py`

A minimal example demonstrating the basic pattern of making a chat completion call and retrieving the response.

## Contributing

When adding new examples:

1. Create a new folder named after the topic
2. Add a single `.py` file with a descriptive name
3. Follow the established `get_response(prompt)` pattern
4. Keep dependencies minimal
5. Print results to stdout for easy inspection
6. Use `temperature=0` and `gpt-4o` unless the example specifically requires different settings

## Troubleshooting

**`NameError: name 'client' is not defined`**
- Make sure you've initialized the OpenAI client at the top of your script:
  ```python
  from openai import OpenAI
  client = OpenAI()
  ```

**401/403 API errors**
- Verify your `OPENAI_API_KEY` is set correctly
- Check that your API key is valid and has available credits
- Never hardcode API keys in your scripts

**Empty or None responses**
- Inspect the `response.choices` structure before indexing
- Check the OpenAI API status if issues persist

## License

[MIT License Copyright (c) 2025](./LICENSE)
