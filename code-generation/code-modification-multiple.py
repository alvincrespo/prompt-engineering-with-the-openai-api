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
Modify the script delimited by triple backticks as follows:
- Let user input parameters interactively
- Make sure to verify inputs are positive, otherwise, display a message for the user, and ask them to provide their input again.
```{script}```
"""

response = get_response(prompt)
print(response)

# Output:
# Here's a modified version of the script that allows the user to input quarterly sales interactively, verifies that the inputs are positive, and prompts the user to re-enter the values if they are not:

# ```python
# def get_positive_input(prompt):
#     while True:
#         try:
#             value = float(input(prompt))
#             if value < 0:
#                 print("Please enter a positive number.")
#             else:
#                 return value
#         except ValueError:
#             print("Invalid input. Please enter a numeric value.")

# quarterly_sales = []
# for i in range(1, 5):  # For 4 quarters
#     sales = get_positive_input(f"Enter sales for quarter {i}: ")
#     quarterly_sales.append(sales)

# total_sales = sum(quarterly_sales)
# print("Total Sales:", total_sales)
# ```

# ### Explanation:
# 1. **Function `get_positive_input`**: This function prompts the user for input and checks if the input is a positive number. If the input is invalid (negative or non-numeric), it displays an error message and asks for input again.
# 2. **Loop for Input**: A loop runs four times (for four quarters), calling the `get_positive_input` function to collect sales data for each quarter.
# 3. **Calculating Total Sales**: After collecting all inputs, the total sales are calculated and printed.
