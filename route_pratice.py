from flask import Flask, url_for

app = Flask(__name__)


@app.route("/index1")
@app.route("/1", methods=["POST", "GET"])
def flask_index():
    return "index"


@app.route("/redrect")
def flask_redrect():
    # return "<a href='/index'>index</a>" 路由反解析  这样修改目标函数路由后就不需要修改对应路由
    return "<a href='%s'>index</a>" % url_for("flask_index")


if __name__ == '__main__':
    # print(app.url_map)
    app.run("127.0.0.1", port=5000)
