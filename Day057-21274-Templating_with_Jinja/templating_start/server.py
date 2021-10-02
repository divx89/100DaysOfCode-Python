import datetime
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", num=random.randint(1, 10),
                           year=datetime.date.today().year, your_name="Random Person")


@app.route("/guess/<name>")
def guess(name):
    age = requests.get("https://api.agify.io", params={"name": name}).json()['age']
    gender = requests.get("https://api.genderize.io", params={"name": name}).json()['gender']
    return render_template("guess.html", name=name.title(), age=age, gender=gender)


@app.route("/blog")
def get_blog():
    return render_template("blog.html", posts=requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json())


if __name__ == "__main__":
    app.run(debug=True)
