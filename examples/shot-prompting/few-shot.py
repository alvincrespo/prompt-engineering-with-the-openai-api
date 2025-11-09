from utils.openai_client import get_response

prompt = """
Text: Today the weather is fantastic -> Classification: positive
Text: The furniture is small -> Classification: neutral
Text: I don't like your attitude -> Classification: negative
Text: That shot selection was awful -> Classification:
"""

print(get_response(prompt))

# Output:
# Classification: negative
