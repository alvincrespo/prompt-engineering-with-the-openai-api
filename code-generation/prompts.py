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

prompt = f"""
Write a Python function that accepts a list of quarterly sales, and outputs the average sales per quarter. Output only the function code.
"""

response = get_response(prompt)
print(response)

# Output:
# def average_quarterly_sales(sales):
#     if not sales:
#         return 0
#     return sum(sales) / len(sales)
