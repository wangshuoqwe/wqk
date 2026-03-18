import os
import requests
from dotenv import load_dotenv

# 加载环境变量（需在项目根目录创建 .env 文件）
load_dotenv()

API_KEY = os.getenv("ARK_API_KEY")
BOT_ID = os.getenv("BOT_ID")  # 或模型 endpoint ID
API_URL = "https://ark.cn-beijing.volces.com/api/v3/bots/chat/completions"  # 火山引擎方舟示例URL，具体以官方文档为准

def chat_with_deepseek(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "bot_id": BOT_ID,
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }
    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"调用失败：{e}"

if __name__ == "__main__":
    print("DeepSeek Chatbot 已启动（输入 'exit' 退出）")
    while True:
        user_input = input("\n用户：")
        if user_input.lower() == "exit":
            break
        reply = chat_with_deepseek(user_input)
        print(f"DeepSeek：{reply}")
