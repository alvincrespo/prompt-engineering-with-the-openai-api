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

text = "Dear sir, I wanted too discus a potentiel opporuntiy for colaboration. Pls let me know wen you're avialable."

prompt = f"""
Proofread the text delimited by triple backticks while keeping the original text structure intact:
```{text}```
"""

print(get_response(prompt))

# Output:
# Dear sir, I wanted to discuss a potential opportunity for collaboration. Please let me know when you're available.
