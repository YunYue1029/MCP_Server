import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def predict_speech(arguments):
    """step by step"""
    user_text = arguments.get("text", "")
    if not user_text:
        return {"error": "Missing 'text' in arguments."}

    system_prompt = """
    你是一個英文母語老師。
    請根據使用者輸入的英文句子，判斷這個句子是否正確，
    如果是正確的句子，請直接回傳這個句子。
    如果不是正確的句子，請推測使用者想要表達的句子，並且回傳這個推測的句子。
    你可以使用上下文的語境來推測使用者的意圖。
    如果無法推測出正確的句子，請回傳“”I don't understand what you want to say.。
    回傳以下 JSON 格式的資訊：
    {
        "pridect_speech": "推測的句子"
    }
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"原始句子：{user_text}"}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content