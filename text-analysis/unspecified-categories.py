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

text = "I bought your XYZ Smart Watch and wanted to share my positive experience. Impressed with it's sleek design, comfort, and touchscreen usability."


prompt = f"""
Classify the sentiment o the text delimited by triple backticks. Give your answer as single word:
```{text}```
"""

response = get_response(prompt)
print(response)

# Output:
# Positive
