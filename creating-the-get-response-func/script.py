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

# Note: gpt-5-mini triggers this 400 error from the API:
# "Unsupported value: 'temperature' does not support 0 with this model. Only the default (1) value is supported."


response = get_response("Create a poem about ChatGPT.")
print(response)
