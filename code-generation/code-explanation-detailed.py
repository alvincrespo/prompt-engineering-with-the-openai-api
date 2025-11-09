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
Explain what the code delimited by triple backticks does.
Let's think step by step.
```{code}```
"""

response = get_response(prompt)
print(response)

# Output:
# Let's break down the code step by step:

# 1. **Function Definition**:
#    ```python
#    def compute_average_sales_per_quarter(sales):
#    ```
#    This line defines a function named `compute_average_sales_per_quarter`. The function takes one parameter, `sales`, which is expected to be a list (or another iterable) of sales figures.

# 2. **Calculating Total Sales**:
#    ```python
#    average_sales = sum(sales) / len(sales)
#    ```
#    - `sum(sales)`: This part calculates the total of all the sales figures in the `sales` list. The `sum()` function adds up all the elements in the iterable.
#    - `len(sales)`: This part calculates the number of elements in the `sales` list. The `len()` function returns the count of items in the iterable.
#    - The division `sum(sales) / len(sales)` computes the average sales by dividing the total sales by the number of sales entries.

# 3. **Returning the Result**:
#    ```python
#    return average_sales
#    ```
#    This line returns the computed average sales value to the caller of the function.

# ### Summary:
# The function `compute_average_sales_per_quarter` takes a list of sales figures as input, calculates the average of those figures, and returns the average. It assumes that the `sales` list is not empty, as dividing by zero (if `len(sales)` is 0) would raise an error.
