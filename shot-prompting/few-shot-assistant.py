from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file automatically

client = OpenAI()  # uses OPENAI_API_KEY from env

def get_response(messages):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature = 0)
  return response.choices[0].message.content

messages = [
  {"role": "user", "content": "Text: Today the weather is fantastic"},
  {"role": "assistant", "content": "positive"},
  {"role": "user", "content": "Text: I don't like your attitude"},
  {"role": "assistant", "content": "negative"},
  {"role": "user", "content": "Text: That shot selection was awful"}
]

response = get_response(messages)
print(response)

# Output:
# negative
