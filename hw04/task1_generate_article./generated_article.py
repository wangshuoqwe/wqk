import os
from openai import OpenAI

# 使用 DeepSeek（免费，需注册获取 key）
client = OpenAI(
    api_key="你的密钥",
    base_url="https://api.deepseek.com"
)

prompt = """
Write an English news article (at least 200 words) about how large language models are changing scientific research. Include a title, three key benefits, and a realistic example.
"""

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=600
)

article = response.choices[0].message.content
print(article)

with open("generated_article.txt", "w", encoding="utf-8") as f:
    f.write(article)
