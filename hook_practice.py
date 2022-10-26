from flask import Flask

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("before_first_request")


@app.before_request
def before_request():
    print("before_first_request")


@app.after_request
def after_request(resp):
    print("after_request")
    return resp


@app.teardown_request
def teardown_req(resp):
    print("teardown_req")
    return resp


@app.route("/")
def index():
    return "index"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
