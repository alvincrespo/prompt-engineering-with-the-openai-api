from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # loads .env file automatically

client = OpenAI()  # uses OPENAI_API_KEY from env

def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature = 0)
  return response.choices[0].message.content

text = "I bought your XYZ Smart Watch and wanted to share my positive experience. Impressed with it's sleek design, comfort, and touchscreen usability."

# Test the function with your prompt
prompt = f"""
Classify the sentiment o the text delimited by triple backticks. Give your answer as single word:
```{text}```
"""

response = get_response(prompt)
print(response)

# Output:
# Positive
