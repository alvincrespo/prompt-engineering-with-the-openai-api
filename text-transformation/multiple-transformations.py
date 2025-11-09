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

text = "omg, I can't believe how awesome this product is! It's like the best thing ever! You guys gotta try it out!"

prompt = f"""
Transform the text delimited by triple backticks with the following two steps:
Step 1 - Proofread it without changing its structure
Step 2 - Change the tone to be professional
```{text}```
"""

print(get_response(prompt))

# Output:
# Step 1 - Proofread:
# I can't believe how impressive this product is! It's one of the best things ever! You all should try it out!

# Step 2 - Change the tone to be professional:
# I am truly impressed by the quality of this product. It stands out as one of the best options available. I highly recommend that you consider trying it.
