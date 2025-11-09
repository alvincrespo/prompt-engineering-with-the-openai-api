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

code = """
def compute_average_sales_per_quarter(sales):
  average_sales = sum(sales) / len(sales)
  return average_sales
"""

prompt = f"""
Explain in one sentence what the code delimited by triple backticks does.
```{code}```
"""

response = get_response(prompt)
print(response)

# Output:
# The code defines a function that calculates and returns the average sales from a list of sales figures provided as input.
