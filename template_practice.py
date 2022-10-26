from flask import Flask, render_template

app = Flask(__name__)

# 装饰器增加自定义的过滤器
# 自定义过滤器实现在线人数统计
@app.template_filter("count")
def filter_count_user(lst):
    return len(lst)

# 使用add_template_filter增加过滤器
# app.add_template_filter(filter_count_user, "count")


@app.route("/")
def index():
    content = {
        "name": "ming",
        "user_gender": ["man", "female"],
        "user_count": ["a", "b", "c"]  # 在线人数列表
    }
    # return render_template("index.html", name="ming")
    return render_template("index.html", **content)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
