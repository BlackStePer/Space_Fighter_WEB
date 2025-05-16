from datetime import datetime
from flask import request
from flask_restful import reqparse, abort, Api, Resource

def comment_time():
    months = {
        "01": "января",
        "02": "февраля",
        "03": "марта",
        "04": "апреля",
        "05": "мая",
        "06": "июня",
        "07": "июля",
        "08": "августа",
        "09": "сентября",
        "10": "октября",
        "11": "ноября",
        "12": "декабря"
    }
    time = str(datetime.utcnow()).split()[0].split("-")[::-1]
    time[1] = months[time[1]]
    return " ".join(time)

def add_comment(user_name, text):
    with open("comments.txt", "a", encoding="UTF-8") as f:
        f.write(user_name.strip() + "\t" + text.strip() + "\t" + comment_time() + "\n")

def all_comments():
    with open("comments.txt", "r", encoding="UTF-8") as f:
        return [s.split("\t") for s in f.readlines()]


class NewComment(Resource):
    def post(self):
        data = request.get_json()

        user = data.get("user")
        comment = data.get("comment")
        if len(user) <= 40:
            add_comment(user, comment)
            return "Коментарий добавлен на сайт"
        else:
            return "Имя пользователя не должно превышать 40 символов"
