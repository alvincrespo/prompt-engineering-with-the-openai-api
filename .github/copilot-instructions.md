# Copilot instructions for this repository

Purpose and scope
- This repo hosts small, self-contained Python scripts that demonstrate prompt engineering patterns using the OpenAI API.
- Each topic lives in its own folder and exposes a single runnable script.

Repository layout (current example)
- `introduction-to-prompt-engineering-best-practices/introduction-to-prompt-engineering.py` — minimal example that wraps a chat completion call in a helper and prints the result.

Core coding pattern
- Use a thin helper function `get_response(prompt: str) -> str` that:
  - Calls `client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}], temperature=0)`
  - Returns `response.choices[0].message.content`
- Keep scripts directly runnable (top-level snippet calling the helper and printing to stdout).

OpenAI client setup (required)
- The examples assume an initialized `client` from the OpenAI Python SDK and an `OPENAI_API_KEY` in the environment.
- Initialize before using `get_response`:

  ```python
  from openai import OpenAI
  client = OpenAI()
  ```

Dependencies and runtime
- Python 3.10+ recommended; install dependencies per example needs (currently just `openai`).
- Quickstart (bash):

  ```bash
  python3 -m venv .venv
  source .venv/bin/activate
  pip install openai
  export OPENAI_API_KEY=sk-...
  python introduction-to-prompt-engineering-best-practices/introduction-to-prompt-engineering.py
  ```

Conventions used in this repo
- Deterministic runs by default: `temperature=0`.
- Default model: `gpt-4o` for examples unless a script states otherwise.
- Minimal structure: one helper + one top-level call; prefer standard library and keep examples dependency-light.
- Output visible on stdout for easy inspection; avoid extra logging unless necessary for the lesson.

Adding a new example script
- Create a new folder named after the topic; add a single `.py` file.
- Reuse the `get_response(prompt)` pattern and initialize `client` at the top of the file.
- Provide a small, hard-coded demo prompt or accept a CLI arg; always print the result to stdout.

Debugging tips specific to this repo
- `NameError: name 'client' is not defined` → Add the `from openai import OpenAI; client = OpenAI()` initialization.
- 401/403 from API → Check `OPENAI_API_KEY` is set and valid; avoid hardcoding secrets in code.
- Empty/None content → Inspect `response.choices` structure before indexing.

Examples (from the codebase)
- Helper function shape:

  ```python
  def get_response(prompt):
      response = client.chat.completions.create(
          model="gpt-4o",
          messages=[{"role": "user", "content": prompt}],
          temperature=0,
      )
      return response.choices[0].message.content
  ```

Guidance for AI agents
- Follow the patterns above; don’t introduce frameworks or complex scaffolding.
- Prefer small, composable scripts with explicit API calls and clear outputs.
- If you need to evolve the pattern, keep it backwards-compatible with existing examples, or add a new folder to illustrate the variant.
