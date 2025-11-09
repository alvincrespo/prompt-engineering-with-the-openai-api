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

script = """
quarterly_sales = [150, 180, 200, 170]
total_sales = sum(quarterly_sales)
print("Total Sales:", total_sales)
"""

prompt = f"""
Modify the script delimited by triple backticks to a function that we can call to compute the total sales given quarterly sales
```{script}```
"""

response = get_response(prompt)
print(response)

# Output:
# You can modify the script into a function that takes a list of quarterly sales as an argument and returns the total sales. Here’s how you can do it:

# ```python
# def compute_total_sales(quarterly_sales):
#     total_sales = sum(quarterly_sales)
#     return total_sales

# # Example usage
# quarterly_sales = [150, 180, 200, 170]
# total_sales = compute_total_sales(quarterly_sales)
# print("Total Sales:", total_sales)
# ```

# In this version, the `compute_total_sales` function calculates the total sales from the provided list of quarterly sales and returns the result. You can call this function with any list of quarterly sales to get the total.
