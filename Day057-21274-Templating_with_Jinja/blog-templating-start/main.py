import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json())


@app.route("/post/<int:num>")
def get_post(num):
    all_posts = requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json()
    for a_post in all_posts:
        if a_post['id'] == num:
            the_post = a_post
    return render_template("post.html", blog_post=the_post)


if __name__ == "__main__":
    app.run(debug=True)
