from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    global reps

    window.after_cancel(timer)
    check_label.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "normal"))
    timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps

    reps += 1

    if reps % 8 == 0:
        timer_label.config(text="Break", fg=RED)
        count_down(int(LONG_BREAK_MIN * 60))
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg=PINK)
        check_label.config(text="✔" * int(reps / 2))
        count_down(int(SHORT_BREAK_MIN * 60))
    else:
        timer_label.config(text="Work", fg=GREEN)
        count_down(int(WORK_MIN * 60))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    canvas.itemconfig(timer_text, text=f"{count // 60}:{count % 60:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# Create Window & give it a title
window = Tk()
window.title("Pomodoro")
# The tomato image is 200x223, and we pad its x and y coordinates to
# give some space to the sides, top and bottom
# Set the background colour to YELLOW
window.configure(padx=100, pady=50, bg=YELLOW)

# Create a canvas of dimensions equal to the image's dimensions
# Set the canvas' background colour to YELLOW, to match that of the window
# The canvas has a border, which has a thickness. If we leave it as it is, the canvas has
# a yellow colour, white border, and then a yellow background color for the window
# So, we set the highlight thickness property to 0
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# Create a PhotoImage object which will then be used as the canvas' image
tomato_image = PhotoImage(file="tomato.png")

# Put the tomato image at x,y coordinates approximately in the middle of the canvas.
canvas.create_image(100, 112, image=tomato_image)

# Create some text and put it at the top of the canvas
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Pack the canvas to display it on the window
canvas.grid(column=1, row=1)

# Create start button
start_button = Button(text="Start", command=start_timer)
start_button.configure(bg="white", fg="black", font=(FONT_NAME, 9, "bold"), highlightthickness=0)
start_button.grid(column=0, row=2)

# Create start button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.configure(bg="white", fg="black", font=(FONT_NAME, 9, "bold"), highlightthickness=0)
reset_button.grid(column=2, row=2)

# Create the check label
check_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 12, "normal"))
check_label.grid(column=1, row=3)

# Create the Timer Label
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

window.mainloop()
