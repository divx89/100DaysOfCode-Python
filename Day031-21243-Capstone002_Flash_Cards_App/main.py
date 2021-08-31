from tkinter import *

import pandas
import random

from pandas import DataFrame

BACKGROUND_COLOR = "#B1DDC6"
canvas_property = {
    "front": {"image": None,
              "language": "Spanish",
              "fill_color": "black"},
    "back": {"image": None,
             "language": "English",
             "fill_color": "white"},
    "current_word": {}
}
timer = None

# ---------------------- Set up Data ------------------------- #
try:
    data_frame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data_frame = pandas.read_csv("./data/spanish_words.csv")

words_to_learn = data_frame.to_dict(orient='records')


# --------------------Set up Functions ---------------------- #
def get_new_word():
    global canvas_property
    canvas_property["current_word"] = words_to_learn[random.randint(0, len(words_to_learn) - 1)]


def display_word(language):
    canvas.itemconfig(language_text, text=f"{language}")
    canvas.itemconfig(word_text, text=f"{canvas_property['current_word'][language]}")


def show_canvas(side):
    canvas.itemconfig(canvas_pic, image=canvas_property[side]['image'])
    canvas.itemconfig(language_text, fill=canvas_property[side]['fill_color'])
    canvas.itemconfig(word_text, fill=canvas_property[side]['fill_color'])
    display_word(canvas_property[side]['language'])


def start_timer():
    global timer
    timer = window.after(3000, show_canvas, "back")


def stop_timer():
    global timer
    window.after_cancel(timer)


def refresh_canvas():
    if timer:
        stop_timer()
    get_new_word()
    show_canvas("front")
    start_timer()


def unknown_answer():
    refresh_canvas()


def known_answer():
    words_to_learn.remove(canvas_property["current_word"])
    new_frame: DataFrame = pandas.DataFrame(words_to_learn)
    new_frame.to_csv(path_or_buf="./data/words_to_learn.csv", index=False)
    refresh_canvas()


# ---------------------- UI Components ----------------------- #
window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_property["front"]["image"] = PhotoImage(file="./images/card_front.png")
canvas_property["back"]["image"] = PhotoImage(file="./images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_pic = canvas.create_image(400, 262, image=canvas_property["front"]["image"])
canvas.grid(column=0, row=0, columnspan=2)

language_text = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))

refresh_canvas()

known_btn_img = PhotoImage(file="./images/right.png")
known_btn = Button(image=known_btn_img, highlightthickness=0, command=known_answer)
known_btn.grid(column=1, row=1)

unknown_btn_img = PhotoImage(file="./images/wrong.png")
unknown_btn = Button(image=unknown_btn_img, highlightthickness=0, command=unknown_answer)
unknown_btn.grid(column=0, row=1)

window.mainloop()
# ------------------------------------------------------------ #
