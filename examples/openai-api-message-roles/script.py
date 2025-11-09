from utils.openai_client import get_response

conversation_messages = [
  {"role": "system", "content": "You are a helpful event management assistant."},
  {"role": "user", "content": "What are some good conversation starters at networking events?"},
  {"role": "assistant", "content": ""}
]

print(get_response(conversation_messages))

# Output
# Here are some effective conversation starters you can use at networking events:

# 1. **Ask About Their Work:**
#    - "What inspired you to get into your field?"
#    - "What projects are you currently working on that excite you?"

# 2. **Discuss the Event:**
#    - "What brought you to this event today?"
#    - "Have you attended this event before? What did you think of it?"

# 3. **Share Insights:**
#    - "I recently read an interesting article about [topic]. Have you come across anything similar?"
#    - "What trends are you seeing in our industry right now?"

# 4. **Personal Interests:**
#    - "What do you enjoy doing outside of work?"
#    - "Have you read any good books or watched any interesting shows lately?"

# 5. **Future Aspirations:**
#    - "What are your professional goals for the next year?"
#    - "Is there a skill you’re currently working on or would like to develop?"

# 6. **Mutual Connections:**
#    - "Do you know [mutual contact]? I recently spoke with them about [topic]."
#    - "I heard you work with [company]. I’ve been wanting to learn more about their work."

# 7. **Industry Challenges:**
#    - "What do you think is the biggest challenge facing our industry right now?"
#    - "How do you see our field evolving in the next few years?"

# 8. **Networking Goals:**
#    - "What are you hoping to achieve by networking at this event?"
#    - "Are there specific people or companies you’re looking to connect with today?"

# 9. **Fun Icebreakers:**
#    - "If you could have dinner with any historical figure, who would it be and why?"
#    - "What’s the best piece of advice you’ve ever received?"

# 10. **Feedback on the Event:**
#     - "What do you think of the speakers/panels so far?"
#     - "Have you found any valuable connections here today?"

# Using these starters can help break the ice and lead to more meaningful conversations. Remember to listen actively and engage with follow-up questions!
