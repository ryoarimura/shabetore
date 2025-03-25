import google.generativeai as genai

# 取得したAPIキーを設定
API_KEY = "AIzaSyDV7N4GqiaHZsLHYk4f0M9daFcG1Vqha0Q"
genai.configure(api_key=API_KEY)


# Gemini プロンプト
def generate_interview_questions(information, context):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    prompt = f"""
    以下の文章は、面接を受ける人の名前、志望企業、学生時代に力を入れたこと、就活の軸です。これらの情報をもとに、企業の面接官が聞きそうな質問を1つ作成してください。

    "{information}"

    {context} 

    【想定質問】
    """
    response = model.generate_content(prompt)
    return response.text
