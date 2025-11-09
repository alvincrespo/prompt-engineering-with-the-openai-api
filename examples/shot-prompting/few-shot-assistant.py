from utils.openai_client import get_response

messages = [
  {"role": "user", "content": "Text: Today the weather is fantastic"},
  {"role": "assistant", "content": "positive"},
  {"role": "user", "content": "Text: I don't like your attitude"},
  {"role": "assistant", "content": "negative"},
  {"role": "user", "content": "Text: That shot selection was awful"}
]

print(get_response(messages))

# Output:
# negative
