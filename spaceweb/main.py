from flask import Flask, render_template, url_for, request, redirect
from funcs import *
from werkzeug.utils import redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/coments", methods=["POST", "GET"])
def coments():
    if request.method == "POST":
        text = request.form['text']

        try:
            add_comment(text)
            return redirect("/coments")
        except:
            return "При добавлении коментария произошла ошибка"
    else:
        return render_template("coments.html", comments=all_comments())


if __name__ == "__main__":
    app.run(debug=False)
