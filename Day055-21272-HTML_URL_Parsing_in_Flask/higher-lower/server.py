import random
from flask import Flask

a_number = random.choice(range(0, 10))
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:number>")
def guess_number(number):
    if number < a_number:
        h1 = "Too low. Try again!"
        color = "red"
        img = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    elif number > a_number:
        h1 = "Too high. Try again!"
        color = "purple"
        img = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    else:
        h1 = "You found me!"
        color = "green"
        img = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"

    return f'<h1 style="color:{color};">{h1}</h1>' \
           f'<img src={img}>'


if __name__ == '__main__':
    app.run(debug=True)
