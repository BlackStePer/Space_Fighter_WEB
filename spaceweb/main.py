from flask import Flask, render_template, url_for, request, redirect
from funcs import *
from werkzeug.utils import redirect

app = Flask(__name__)
api = Api(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/characters")
def characters():
    return render_template("characters.html")

@app.route("/coments", methods=["POST", "GET"])
def coments():
    if request.method == "POST":
        user_name = request.form["user"]
        text = request.form['text']
        if len(user_name.strip()) > 40:
            return render_template("coments.html", comments=all_comments(), much=True)

        try:
            add_comment(user_name, text)
            return redirect("/coments")
        except:
            return "При добавлении коментария произошла ошибка"
    else:
        return render_template("coments.html", comments=all_comments(), much=False)


api.add_resource(NewComment, '/api/com')

if __name__ == "__main__":
    app.run(debug=False)
