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

text = "Hey there! Check out our awesome summer deals! They're super cool, and you won't want to miss them. Grab 'em now!"

prompt = f"""Write the text delimited by triple backticks using a formal and persuasive tone:
```{text}```
"""

print(get_response(prompt))

# Output:
# Dear Valued Customer,

# We are pleased to present our exceptional summer deals, which are designed to provide you with outstanding value and quality. These offers are truly remarkable, and we encourage you to take advantage of them before they expire. Seize this opportunity to enhance your summer experience.

# Best regards,
# [Your Company Name]
