from flask import Flask, make_response, request, jsonify

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def index():
    name = request.form.get("name")
    resp = make_response("index")
    resp.set_cookie("name", name, max_age=3600)
    return resp


@app.route("/delete_cookie", methods=["POST"])
def del_cookie():
    name = request.form.get("name")
    resp = make_response()
    resp.delete_cookie(name)
    return resp


@app.route("/get_cookie", methods=["POST"])
def get_cookie():
    name = request.cookies.get("name")
    return jsonify({"code": 200, "msg": name})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
