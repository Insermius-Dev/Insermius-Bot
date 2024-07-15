from threading import Thread
from flask import Flask, render_template

app = Flask("")


@app.route("/")
def index():
    return render_template("index.html", contributors=contributors, helpers=helpers, developer=developer)
    # return render_template("index.html")


def run():
    app.run(host="0.0.0.0", port=8080)


def start(contr, hlpr, dev) -> None:
# def start():
    global contributors
    global helpers
    global developer

    contributors = contr
    helpers = hlpr
    developer = dev

    t = Thread(target=run)
    t.start()


if __name__ == "__main__":
    start()