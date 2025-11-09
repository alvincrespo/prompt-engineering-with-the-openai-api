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

  examples = """
  Input: [150000, 180000, 200000, 170000] -> Output: 175000.0
  Input: [10000, 25000, 30000, 15000] -> Output: 20000.0
  Input: [50000, 75000, 60000, 45000] -> Output: 57500.0
  """

  prompt = f"""
  You are provided with input-output examples delimited by triple backticks for a python program that receives a list of quarterly sales data. Write code for this program.
  ```{examples}```
  """

  response = get_response(prompt)
  print(response)

  # Output:
  # To calculate the average quarterly sales from a list of sales data, you can use the following Python program. This program takes a list of quarterly sales as input and returns the average sales value.

  # Here's the code:

  # ```python
  # def average_quarterly_sales(sales):
  #     if not sales:
  #         return 0.0  # Return 0.0 if the list is empty
  #     return sum(sales) / len(sales)

  # # Example usage:
  # print(average_quarterly_sales([150000, 180000, 200000, 170000]))  # Output: 175000.0
  # print(average_quarterly_sales([10000, 25000, 30000, 15000]))     # Output: 20000.0
  # print(average_quarterly_sales([50000, 75000, 60000, 45000]))     # Output: 57500.0
  # ```
  #
  ### Explanation:
  # - The function `average_quarterly_sales` takes a list of sales as input.
  # - It checks if the list is empty and returns `0.0` if it is.
  # - It calculates the average by summing the sales and dividing by the number of sales entries.
  # - Finally, it returns the average sales value.

  # You can test the function with the provided examples to see the expected outputs.
  # ➜  prompt-engineering-with-the-openai-api git:(main) ✗
