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

text = "Como estas hoy? Espero que todo vaya bien. Estoy aprendiendo a programar en Python y me encanta."


prompt = f"""
You will be provided with a text delimited by triple backticks. If the text is written in English, suggest as suitable title for it. Otherwise, write 'I only understand English.'.
```{text}```
"""

response = get_response(prompt)
print(response)

# Output:
# I only understand English.
