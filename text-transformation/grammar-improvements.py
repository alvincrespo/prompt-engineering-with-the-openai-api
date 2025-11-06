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

text = "Dear sir, I wanted too discus a potentiel opporuntiy for colaboration. Pls let me know wen you're avialable."

prompt = f"""
Proofread the text delimited by triple backticks while keeping the original text structure intact:
```{text}```
"""

print(get_response(prompt))

# Output:
# Dear sir, I wanted to discuss a potential opportunity for collaboration. Please let me know when you're available.
