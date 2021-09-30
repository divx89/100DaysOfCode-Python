from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"

    return wrapper


def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"

    return wrapper


def make_emphasized(function):
    def wrapper():
        return f"<i>{function()}</i>"

    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph</p>' \
           '<img src="https://media.giphy.com/media/aCqb9YW7QclN3rtto5/giphy-downsized-large.gif?' \
           'cid=ecf05e47fetrpw8a3oo6whjvdneoxsqrwd5ir4cgxrru9nn2&rid=giphy-downsized-large.gif&ct=g" width=200>'


# Using a new decorator. See the Decorators/main.py for more info
@app.route("/bye")
@make_bold
@make_emphasized
@make_underline
def say_bye():
    return "bye"


# Here, the variable within <> of the decorator becomes a variable,
# which is passed to the function as an argument
@app.route("/<name>")
def say_name(name):
    return f"My name is {name + '12'}"


# Here, as <> contains "path:", it passes everything, including slashes.
# Default is a string without slashes
@app.route("/user/<path:name>")
def say_a_name(name):
    return f"The name is {name}"


# Here, we have multiple variables
# The first one is default, i.e. String
# The 2nd one is an integer.
# The decorator passes these to the function in the order of their appearance
@app.route("/user/<name>/<int:number>")
def numbered_name(name, number):
    return f"The name is {name}, and the number is {number}"


if __name__ == "__main__":
    # Setting the debug property to True, so that the app reloads
    # automatically when our code changes
    app.run(debug=True)
