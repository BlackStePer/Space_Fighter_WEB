from datetime import datetime

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

def add_comment(text):
    with open("a.txt", "a", encoding="UTF-8") as f:
        f.write(text.strip() + "\t" + comment_time() + "\n")

def all_comments():
    with open("a.txt", "r", encoding="UTF-8") as f:
        return [s.split("\t") for s in f.readlines()]