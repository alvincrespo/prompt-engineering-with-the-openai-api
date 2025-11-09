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

ticket_1 = """
Hello, I'm Emma Adams. I'd like to ask about my reservation with the code CAR123.
You can reach me at +1234567890 if needed.
"""

entities_1 = """
* Customer Details:
  - Name: Emma Adams
  - Phone: +1234567890
* Reservation Details:
  - Reservation Code: CAR123
"""

ticket_2 = """
This is Sarah Williams. I would like to request some information regarding
my upcoming flight with reservation number FLT456. Thank you.
"""

entities_2 = """
* Customer Details:
  - Name: Sarah Williams
* Reservation Details:
  - Reservation Code: FLT456
"""

ticket_3 = """
Hello, I'm David Brown (CUST123). I need assistance with my reservaation under
the code HOTEL456. There are some questions and issues related to my upcoming stay
that require your attention.
"""


prompt = f"""
Text: {ticket_1} -> Entities: {entities_1}
Text: {ticket_2} -> Entities: {entities_2}
Text: {ticket_3} -> Entities:
"""

response = get_response(prompt)
print(response)

# Output:
# * Customer Details:
#   - Name: David Brown
#   - Customer ID: CUST123
# * Reservation Details:
#   - Reservation Code: HOTEL456
