import openai
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def final_output(arguments):
    history = arguments.get("history", [])
    if not history:
        return {"error": "Missing 'history' in arguments."}
    
    prompt = """"請根據以上資料，使用繁體中文整理學生的表現，不要將原本因該是英文的部分翻成中文，並提供清楚的建議。
    輸出請使用 JSON 格式，包含以下欄位：
    spoken_text(學生實際說出的英文句子), 
    differences(提供學生與原文中相異的地方，並且為小寫字母，回傳為一個字串陣列，例如：['bad', 'need']),
    accuracy(準確度百分比),
    suggestion(給學生的繁體中文學習建議，如果錯誤率太高，直接告訴他重新練習)。
    請生成對應 JSON 格式的分析。"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": history + prompt},
            ],
            temperature=0,
        )

        # 取出 GPT 回應內容
        content = response.choices[0].message.content.strip()

        # 嘗試解析 JSON
        result = json.loads(content)

        return result
    
    except json.JSONDecodeError as e:
        print("❌ JSON 解析錯誤:", e)
        print("回傳內容:", content)
        return {"error": "JSON 解析失敗"}
    
    except Exception as e:
        print("❌ 發生錯誤:", e)
        return {"error": "GPT 回應錯誤"}