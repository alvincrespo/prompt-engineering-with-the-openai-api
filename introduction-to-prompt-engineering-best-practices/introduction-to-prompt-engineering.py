from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def get_response(prompt):
  response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "user", "content": prompt}
    ],
    temperature=0
  )

  return response.choices[0].message.content


response = get_response("What is prompt engineering?")
print(response)
