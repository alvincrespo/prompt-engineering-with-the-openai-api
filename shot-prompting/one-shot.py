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

prompt = """
Q: Sum the numbers 3, 5, and 6. A: 3+5+6=14.
Q: Sum the numbers 2, 4, and 7. A:
"""

response = get_response(prompt)
print(response)

# Output:
# 2 + 4 + 7 = 13.
