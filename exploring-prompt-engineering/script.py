from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_response(prompt):

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature = 0)
  return response.choices[0].message.content


prompt = """"
Create a poem about ChatGPT.

The poem should be written in a way that a child can understand in basic English.
"""

response = get_response(prompt)
print(response)
