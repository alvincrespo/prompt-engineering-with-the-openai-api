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

prompt = """
What is prompt engineering?
"""

response = get_response(prompt)
print(response)

# Output:
# Prompt engineering is the process of designing and refining the input prompts given to artificial intelligence models, particularly language models like GPT-3 and its successors, to elicit the most accurate, relevant, and useful responses. It involves crafting the wording, structure, and context of prompts to guide the model's output effectively.

# Key aspects of prompt engineering include:

# 1. **Clarity**: Ensuring that the prompt is clear and unambiguous so that the model understands what is being asked.

# 2. **Specificity**: Providing specific details or constraints in the prompt to narrow down the model's focus and improve the relevance of the response.

# 3. **Context**: Including background information or context that helps the model generate a more informed and appropriate response.

# 4. **Iterative Refinement**: Testing and modifying prompts based on the quality of the responses received, often through trial and error.

# 5. **Use of Examples**: Providing examples within the prompt to illustrate the desired format or type of response.

# Effective prompt engineering can significantly enhance the performance of AI models in various applications, such as content generation, question answering, and conversational agents.
