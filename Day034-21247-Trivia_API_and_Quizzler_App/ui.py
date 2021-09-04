from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR, fg="white")
        self.display_score()
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question = self.canvas.create_text(150, 125,
                                                font=("Arial", 20, "italic"),
                                                fill=THEME_COLOR, width=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(20, 40))

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=lambda: self.check_answer('True'))
        self.false_button = Button(image=false_image, highlightthickness=0, command=lambda: self.check_answer('False'))

        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def change_button_status(self, status):
        self.true_button["state"] = status
        self.false_button["state"] = status

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            canvas_text = self.quiz.next_question()
            self.change_button_status("normal")
        else:
            canvas_text = "You've reached the end of the quiz!"

        self.canvas.itemconfig(self.question, text=canvas_text)

    def display_score(self):
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def change_canvas(self, is_correct: bool):
        self.change_button_status("disabled")
        self.canvas.config(bg="green" if is_correct else "red")
        self.display_score()
        self.window.after(1000, func=self.get_next_question)

    def check_answer(self, answer):
        self.change_canvas(self.quiz.check_answer(answer))
