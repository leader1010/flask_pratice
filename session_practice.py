from flask import Flask, session

app = Flask(__name__)


@app.route("/login")
def login():
    session["name"] = "python"
    return "login success"


@app.route("/")
def index():
    name = session.get("name")
    return name


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
