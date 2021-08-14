class Question(object):
    """ Class Question stores questions, their answers, and methods to manipulate them"""

    def __init__(self, text, answer):
        """Initialize a Question object
            Parameters:
                text (String) - The Text of the Question
                answer (String) - Answer of the question being asked
        """
        self.text = text
        self.answer = answer


