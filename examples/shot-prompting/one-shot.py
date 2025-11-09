from utils.openai_client import get_response

prompt = """
Q: Sum the numbers 3, 5, and 6. A: 3+5+6=14.
Q: Sum the numbers 2, 4, and 7. A:
"""

print(get_response(prompt))

# Output:
# 2 + 4 + 7 = 13.
