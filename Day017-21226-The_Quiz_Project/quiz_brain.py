# TODO: Asking Questions
# TODO: Checking if the answer was correct
# TODO: Checking if we're at the end of the quiz

# Attributes:
#   Question Number
#   Question List

class QuizBrain(object):
    """Class QuizBrain to track questions being asked"""

    def __init__(self, question_list):
        """ Initialize an object of type QuizBrain
            Parameters:
                question_list (List of Question objects) - List of Question objects
        """
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        """Display the next question in the list and ask for an answer, while incrementing the question number"""
        while True:
            current_question = self.question_list[self.question_number]
            user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True"
                                f"/False)?: ")
            if user_answer.lower() in ['true', 'false']:
                break
            else:
                print("Incorrect choice. Please retry")
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        """Determine if the list of questions has some left to ask"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        """Determine if answer is right or wrong"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! ", end="")
        else:
            print("That's wrong. ", end="")
        print(f"The correct answer was {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
