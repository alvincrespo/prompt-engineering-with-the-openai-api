from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Create the OpenAI client: you can leave "<OPENAI_API_TOKEN>" as is
client = OpenAI()

# Define the conversation messages
conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {"role": "user", "content": "What are some good conversation starters at networking events?"},
    {"role": "assistant", "content": ""}
]

response = client.chat.completions.create(
  model="gpt-5-nano",
  messages=conversation_messages
)
print(response.choices[0].message.content)
