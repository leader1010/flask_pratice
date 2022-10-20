from flask import Flask, url_for
from werkzeug.routing import BaseConverter
import typing as t

app = Flask(__name__)


@app.route("/<name>")
def hello(name):
    return "hello %s" % name


@app.route("/1/<int:id>")
def hello_id(id):
    return f"hello {id}"


class MyConverter(BaseConverter):
    def __init__(self, url_map, *args):
        super().__init__(url_map)
        self.regex = args[0]

    def to_python(self, value: str) -> t.Any:
        """正则匹配后的值传入value，视图函数接收返回值"""
        print(f"value={value}")
        return "666"

    def to_url(self, value: t.Any) -> str:
        """路由反解析时，value接收到urlfor传递的符合正则的参数，返回值拿去路由正则匹配"""
        return "123"


app.url_map.converters["myre"] = MyConverter


@app.route("/3/<myre('\d{3}'):id>")
def hello_id_re(id):
    return f"hello 3 {id}"


@app.route("/super")
def super_converter():
    return "<a href=%s>converter to_url</a>" % url_for("hello_id_re", id=333)


if __name__ == '__main__':
    app.run("127.0.0.1", port=5000, debug=True)
