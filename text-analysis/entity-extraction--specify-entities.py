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

text = """
The XYZ Mobile X200: a sleek 6.5-inch Super AMOLED smartphone with a 48MP
triple-camera, octa-core processor, 5000mAh battery, 5G connectivity, and Android 11 OS.
Secure with fingerprint and facial recognition. 128GB storage, expandable up to 512GB.
"""


prompt = f"""
Identify the following entities from the text delimited by triple backticks:
- Product Name
- Display Size
- Camera Resolution
Format the answer as an unordered list.
```{text}```
"""

response = get_response(prompt)
print(response)

# Output:
# - Product Name: XYZ Mobile X200
# - Display Size: 6.5-inch
# - Camera Resolution: 48MP
