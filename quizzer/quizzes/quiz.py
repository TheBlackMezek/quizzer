"Module containing the Quiz class"
from quizzes.section import Section


class Quiz:
    "Class for storing questions, processing answers, and tracking status"
    def __init__(self) -> None:
        self.title = 'QUIZ_TITLE_NOT_SET'
        "Title of the quiz to be displayed to the user"
        self.correct_answers = 0
        "Number of correct answers given this session"
        self.in_session = False
        "Whether or not a quiz session is in progress"

        self._root_section = Section()
        "Storage for all questions in the quiz"
        self._root_section.title = "root"
        self._current_question = None
        "The active question in the quiz session"
    
    def start_session(self) -> None:
        "Initialize a quiz session"
        self.in_session = True
        self._root_section.__iter__()
        self._current_question = self._root_section.__next__()

    def get_prompt(self) -> str:
        "Return the text prompt for the current question in the session"
        return self._current_question.prompt_text

    def submit_answer(self, answer: str) -> tuple:
        """Submit an answer for the current question in the session\n
        Returns two values: was the answer correct, and what was 
        the correct answer"""
        # Evaluate answer, get return values
        submission_correct = self._current_question.eval(answer)
        true_answer = self._current_question.answer
        # Track number of correct answers
        if submission_correct:
            self.correct_answers += 1
        # Prepare next question, check if session is over
        try:
            self._current_question = self._root_section.__next__()
        except StopIteration:
            self._current_question = None
            self.in_session = False
        # Return answer results
        return (submission_correct, true_answer)
    
    def question_count(self) -> int:
        "Returns the number of questions in the Quiz"
        return self._root_section.question_count()
