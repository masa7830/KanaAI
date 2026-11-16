from flask import Flask, render_template, request, redirect, url_for

from kana import get_reply

from study import (
    start_study,
    stop_study,
    save_progress,
    get_dashboard,
    add_english_stamp,
    add_manual_study
)

app = Flask(__name__)


@app.route("/english/stamp", methods=["POST"])
#URLを登録する
def english_stamp():
#関数を実行する
    category = request.form.get(
        "category",
        "単語帳"
    )

    add_english_stamp(category)

    return redirect(url_for("home"))


@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        reply = get_reply(message)

    dashboard = get_dashboard()
    #ダッシュボードから受け取ってHTMLに渡す
    
    return render_template(
        "index.html",
        reply=reply,
        dashboard=dashboard
    )


@app.route("/study/start", methods=["POST"])
def study_start():

    category = request.form.get("category", "Kana開発")
    mode = request.form.get("mode", "countup")
    target_seconds = request.form.get("target_seconds", 0)

    target_seconds = int(target_seconds)
    #読み込んだ文字列を整数に変換
    start_study(category,mode,target_seconds)

    return redirect(url_for("home"))


@app.route("/study/stop", methods=["POST"])
def study_stop():

    stop_study()

    return redirect(url_for("home"))


@app.route("/study/progress", methods=["POST"])
def study_progress():

    progress = request.form.get(
        "progress",
        ""
    )

    save_progress(progress)

    return redirect(url_for("home"))

@app.route("/study/manual", methods=["POST"])
def study_manual():

    category = request.form.get("category", "Python")
    minutes = request.form.get("minutes", "")
    #フォームから値を受け取る
    try:
        minutes = int(minutes)

        if minutes <= 0:
            return redirect(url_for("home"))
        #0以下なら終了してトップページに戻る
    except ValueError:
        return redirect(url_for("home"))
        #エラーならトップページに戻る
    add_manual_study(category, minutes)
    #学習履歴に追加
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)