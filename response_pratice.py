from flask import Flask, make_response, jsonify, redirect, url_for

app = Flask(__name__)


@app.route("/")
def index():
    resp = make_response("index page")
    resp.headers["Content-Type"] = "application/json"
    resp.status = "200"  # "200 Ok"
    return resp


@app.route("/person")
def get_person():
    p = {
        "name": "ming",
        "age": 22
    }
    # (请求体 状态码 请求头)
    # return json.dumps(p), 200, {"Content-Type": "application/json"}
    # jsonify帮助我们将数据转换为json字符串，并设置响应头{"Content-Type": "application/json"}
    return jsonify(p)


@app.route("/login")
def login():
    return redirect(url_for("index"))  # code:302


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
