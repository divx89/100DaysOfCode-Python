import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_index():
    return render_template("index.html", posts=requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json())


@app.route("/<page_name>")
def get_page(page_name):
    return render_template(f"{page_name}.html")


@app.route("/post/<int:num>")
def get_post(num):
    posts = requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json()
    post = [post for post in posts if post['id'] == num][0]
    return render_template("post.html", blog_post=post)


if __name__ == "__main__":
    app.run(debug=True)
