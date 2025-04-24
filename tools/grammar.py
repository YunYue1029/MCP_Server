import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def grammar_check(arguments):
    user_text = arguments.get("text", "")
    if not user_text:
        return {"error": "Missing 'text' in arguments."}

    system_prompt = """你是一個英文文法分析助手。請根據使用者輸入的英文句子，回傳以下 JSON 格式的資訊：
    {
        "grammar_issues": [
            {
            "error": "描述文法錯誤",
            "suggestion": "建議的修改方式"
            }
        ],
        "original_sentence": "原始句子",
        "suggested_sentence": "修正後的完整句子",
    }
    請使用繁體中文解釋內容。
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