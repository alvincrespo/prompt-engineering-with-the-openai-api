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
Generate a list containing ONLY the names of the top 5 cities to visit in 2026.
"""

response = get_response(prompt)
print(response)

# Output:
# 1. Tokyo
# 2. Barcelona
# 3. New York City
# 4. Paris
# 5. Sydney
