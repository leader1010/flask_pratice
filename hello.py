from flask import Flask, current_app

app = Flask(__name__)
# falsk会自动到static中寻找静态资源，默认路由前缀为static
# 可以利用static_url_path，修改前缀参数
# app = Flask(__name__,
#             static_url_path="/python",
#             static_folder="/static",
#             template_folder="templates")

# 为flask添加配置参数
app.config.from_pyfile("Myconfig.cfg")


# 通过对象的方式配置
class Myconfig(object):
    """配置文件"""
    DEBUG = True
    TEST = 11


app.config.from_object(Myconfig)


@app.route("/")
def hello():
    # 在视图中获取 且视图函数和flask app在同一py文件 否则使用current_app
    print(app.config.get("TEST"))
    return "hello flask"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080)
