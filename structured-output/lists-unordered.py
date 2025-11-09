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
Generate an unordered list containing ONLY the names of the top 5 cities to visit in 2026.
"""

response = get_response(prompt)
print(response)

# Output:
# - Tokyo
# - Barcelona
# - New York City
# - Sydney
# - Cape Town
