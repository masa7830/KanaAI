from flask import Flask, render_template, request, redirect, url_for

from kana import get_reply

from study import (
    start_study,
    stop_study,
    save_progress,
    get_dashboard
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    reply = ""

    if request.method == "POST":
        message = request.form.get("message", "")
        reply = get_reply(message)

    dashboard = get_dashboard()

    return render_template(
        "index.html",
        reply=reply,
        dashboard=dashboard
    )


@app.route("/study/start", methods=["POST"])
def study_start():

    category = request.form.get(
        "category",
        "Kana開発"
    )

    start_study(category)

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


if __name__ == "__main__":
    app.run(debug=True)