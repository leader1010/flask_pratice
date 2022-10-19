from flask import Flask
from werkzeug.routing import BaseConverter

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


app.url_map.converters["myre"] = MyConverter


@app.route("/3/<myre('\d{3}'):id>")
def hello_id_re(id):
    return f"hello 3 {id}"


if __name__ == '__main__':
    app.run("127.0.0.1", port=5000)
