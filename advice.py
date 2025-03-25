import os
import google.generativeai as genai

# 取得したAPIキーを設定
API_KEY = "AIzaSyDV7N4GqiaHZsLHYk4f0M9daFcG1Vqha0Q"
genai.configure(api_key=API_KEY)


# Gemini プロンプト
def analyze_interview_responses(question, answer):
    model = genai.GenerativeModel("gemini-1.5-pro-latest")

    prompt = f"""
    以下の面接回答を分析し、論理的な一貫性、説得力、簡潔さの観点からそれぞれ2,3文で簡単にフィードバックを提供してください。
    また、より良い回答にするための具体的なアドバイスを3つ記載してください。改善例はいらないです。
    【質問内容】 : {question}
    【回答】: {answer}
    【改善アドバイス】
    """
    result = model.generate_content(prompt)
    print(result.text)

    return result.text


# 使用例
if __name__ == "__main__":

    question = "今までのご経験を交えながら、自己PRをしてください。"
    answer = "私の強みは、問題に対して何度も試行錯誤し、必ず解決に導く根気強さです。前職の営業職では、低迷していた部署全体の売り上げを上げるべく、個人単位での努力を積み重ねてまいりました。結果として、営業成績トップになったことに加え、同僚の指導にも従事し、部署全体の売り上げを前年比150％以上に引き上げることができました。私が営業時に取り組んだのは、お客さまとのコミュニケーションを毎回工夫して、自分なりの潜在ニーズのくみ取り方を確立したことです。それによって、お客さまの立場になって提案することができ、成約につなげることができました。御社では、前職で培ったコミュニケーション力や根気強さを活かして、お客さまと信頼関係を構築していきたいと考えております。"
    feedback = analyze_interview_responses(question, answer)
