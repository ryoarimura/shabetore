from flask import Flask, render_template, request, redirect, url_for
from generate_questions import generate_interview_questions
from text_to_speech import text_to_speech
from record import Recorder
import threading
from mojiokoshi import transcribe_audio
from advice import analyze_interview_responses  # 追加
import markdown

app = Flask(__name__)


@app.route("/")
def index():
    global context, Q, A
    Q = []
    A = []
    context = ""
    # global変数 関数内の壁を越えて、関数と関数でやりとり  　but→localに比べて無駄が多い(処理が遅くなる)
    return render_template("index.html")


@app.route("/generate", methods=["GET", "POST"])
def generate():
    global questions, context, user_input, Q
    if request.method == "POST":
        name = request.form["name"]
        company = request.form["company"]
        gakuchika = request.form["gakuchika"]
        axis = request.form["axis"]

        user_input = f"""[名前]{name}
        [志望企業]{company} 
        [学生時代に力を入れたこと]{gakuchika} 
        [就活の軸]{axis}です。"""

        questions = generate_interview_questions(user_input, context)
        context += questions
        Q.append(questions)
        print(context)
        text_to_speech(questions)

    return render_template("result.html", questions=questions.split("\n"))


@app.route("/record", methods=["POST"])
def record():
    # threading.Thread(target=record_audio).start()
    global recorder
    recorder = Recorder()
    threading.Thread(target=recorder.record_audio).start()

    return redirect(url_for("generate"))


@app.route("/record_end", methods=["POST"])
def record_end():
    global context, user_input, Q, A
    recorder.recording = False
    recorder.audiostop()
    recorder.rec_exec()
    result = transcribe_audio()
    A.append(result)

    context += result
    print(context)

    questions = generate_interview_questions(user_input, context)
    context += questions
    Q.append(questions)
    print(Q)
    print(context)
    text_to_speech(questions)

    return render_template("result.html", questions=questions.split("\n\n"))

    # threading.Thread(target=record_audio).start()


@app.route("/analyze", methods=["POST"])
def analyze():
    global context, Q, A
    feedbacks = []
    print("フィードバック開始")
    for (
        question,
        answer,
    ) in zip(Q[:-1], A):
        feedback = analyze_interview_responses(question, answer)
        feedback = markdown.markdown(feedback)
        feedbacks.append(feedback)
    return render_template("analysis.html", feedbacks=feedbacks, Q=Q[:-1], A=A)


if __name__ == "__main__":
    app.run(debug=True)
