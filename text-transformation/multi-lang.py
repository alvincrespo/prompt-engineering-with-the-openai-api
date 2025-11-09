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

text = "The product combines top quality with a fair price."

prompt = f"""
Translate the English text delimited by triple backticks to French, Spanish and German:
```{text}```
"""

print(get_response(prompt))

# Output:
# Here are the translations:

# **French:** Le produit allie une qualité supérieure à un prix équitable.

# **Spanish:** El producto combina alta calidad con un precio justo.

# **German:** Das Produkt vereint hohe Qualität mit einem fairen Preis.
