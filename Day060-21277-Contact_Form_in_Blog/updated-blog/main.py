import smtplib

import requests
from flask import Flask, render_template, request
from dotenv import dotenv_values

# Load the environment variables
config = dotenv_values(".env")

app = Flask(__name__)


@app.route("/")
def get_index():
    return render_template("index.html", posts=requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json())


@app.route("/<page_name>")
def get_page(page_name):
    return render_template(f"{page_name}.html", msg_sent=False)


@app.route("/post/<int:num>")
def get_post(num):
    posts = requests.get("https://api.npoint.io/416c5f2dd61c4026a4d2").json()
    post = [post for post in posts if post['id'] == num][0]
    return render_template("post.html", blog_post=post)


@app.route("/contact", methods=["POST"])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    with smtplib.SMTP(config['SMTP_SERVER']) as connection:
        connection.starttls()
        connection.login(user=config['EMAIL_ID'], password=config['EMAIL_PASSWORD'])
        message_body = f"Name: {name}\n" \
                       f"Email: {email}\n" \
                       f"Phone: {phone}\n" \
                       f"Message: {message}"
        connection.sendmail(from_addr=config['EMAIL_ID'],
                            to_addrs=config['EMAIL_ID'],
                            msg=f"Subject:New Message\n\n{message_body}".encode("utf-8"))
    return render_template("contact.html", msg_sent=True)


if __name__ == "__main__":
    app.run(debug=True)
