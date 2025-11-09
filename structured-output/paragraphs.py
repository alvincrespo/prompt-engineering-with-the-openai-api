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


prompt = """"
Provide a structured paragraph with clear headings and subheadings about the benefits of regular exercise on overall health and well-being.
"""

response = get_response(prompt)
print(response)

# Output:

"""
# Benefits of Regular Exercise on Overall Health and Well-Being

## Physical Health

Regular exercise significantly enhances physical health by improving cardiovascular fitness, strengthening muscles, and increasing flexibility. Engaging in consistent physical activity helps to maintain a healthy weight, reduces the risk of chronic diseases such as diabetes and heart disease, and boosts the immune system. Additionally, exercise promotes better sleep patterns, which are crucial for overall health.

## Mental Health

Exercise is also beneficial for mental health, as it has been shown to reduce symptoms of anxiety and depression. Physical activity stimulates the release of endorphins, often referred to as "feel-good" hormones, which can elevate mood and enhance feelings of well-being. Furthermore, regular exercise can improve cognitive function and memory, contributing to better mental clarity and focus.

## Social Well-Being

Participating in group exercises or team sports fosters social connections and a sense of community. This social interaction can lead to improved emotional support and a greater sense of belonging, which are essential for mental well-being. Engaging in physical activities with others can also motivate individuals to maintain their exercise routines, leading to long-term health benefits.

## Conclusion

In summary, regular exercise offers a multitude of benefits that encompass physical health, mental well-being, and social connections. By incorporating consistent physical activity into daily routines, individuals can enhance their overall quality of life and promote long-term health.
"""
