import html


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
        self.current_question = None

    def next_question(self):
        """Display the next question in the list and ask for an answer, while incrementing the question number"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"{html.unescape(self.current_question.text)}"

    def still_has_questions(self):
        """Determine if the list of questions has some left to ask"""
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        """Determine if answer is right or wrong"""
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
