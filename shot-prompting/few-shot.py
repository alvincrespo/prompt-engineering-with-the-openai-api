from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file automatically

client = OpenAI()  # uses OPENAI_API_KEY from env

def get_response(prompt):
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature = 0)
  return response.choices[0].message.content

prompt = """
Text: Today the weather is fantastic -> Classification: positive
Text: The furniture is small -> Classification: neutral
Text: I don't like your attitude -> Classification: negative
Text: That shot selection was awful -> Classification:
"""

response = get_response(prompt)
print(response)

# Output:
# Classification: negative
