from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/query")
def query_args():
    name = request.args.get("name")
    return name


@app.route("/upload", methods=["POST"])
def upload_file():
    pic = request.files.get("pic")
    if not pic:
        return jsonify({"code": 405, "msg": "OK"})
    pic.save("./upload_image.png")
    return jsonify({"code": 200, "msg": "OK"})


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)