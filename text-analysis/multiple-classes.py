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
Identify emotions used in this text. Don't use more than 3 emotions.
Format your answer as a list of words separated by commas:
```{text}```
"""

response = get_response(prompt)
print(response)

# Output:
# positive, impressed, satisfaction
