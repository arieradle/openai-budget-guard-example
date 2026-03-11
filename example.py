from shekel import budget
from openai import OpenAI

# Enforce a daily OpenAI API spending limit
client = OpenAI()

with budget(max_usd=5.0):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "Hello"}]
    )

print(response.choices[0].message.content)