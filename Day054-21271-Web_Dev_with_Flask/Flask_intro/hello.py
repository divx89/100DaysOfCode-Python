from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# Using a new decorator. See the Decorators/main.py for more info
@app.route("/bye")
def say_bye():
    return "bye"
