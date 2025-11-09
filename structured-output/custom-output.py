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

text = "Once upon a time in a quaint little village, there lived a curious young boy named David. David was [...]"

instructions = "You will be provided with a text delimited by triple backticks. Generate a suitable title for it."

output_format = """
Use the following format for the output:
- Text: <text we want to generate>
- Title: <the generated title>
"""


prompt = instructions + output_format + f"```{text}```"

response = get_response(prompt)
print(response)

# Output:
# - Text: Once upon a time in a quaint little village, there lived a curious young boy named David. David was [...]
# - Title: The Adventures of Curious David in a Quaint Village
