from typing import Union, overload
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

@overload
def get_response(prompt: str) -> str: ...

@overload
def get_response(messages: list[dict]) -> str: ...

def get_response(input: Union[str, list[dict]]) -> str:
    """
    Get a response from OpenAI's GPT model using the provided prompt.

    Args:
        prompt (str): The prompt to send to the model

    Returns:
        str: The model's response content
    """
    if isinstance(input, str):
        messages = [{"role": "user", "content": input}]
    else:
        messages = input

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0
    )

    return response.choices[0].message.content

# Note: gpt-5-mini triggers this 400 error from the API:
# "Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported."
