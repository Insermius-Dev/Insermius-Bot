from threading import Thread
from flask import Flask, render_template

app = Flask("")

@app.route("/")
def index():
    return render_template("index.html", contributors=contributors, lilhelpers=lilhelpers, developer=developer)


def run():
    app.run(host="0.0.0.0", port=8080)


def start(contr, lilhelp, dev):
    global contributors
    global lilhelpers
    global developer
    contributors = contr
    lilhelpers = lilhelp
    developer = dev
    t = Thread(target=run)
    t.start()