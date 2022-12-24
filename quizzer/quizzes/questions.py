"Module containing classes for quiz questions"


class Question:
    """Base class for different question types"""
    def __init__(
            self,
            prompt_text: str = 'TEXT_PROMPT_NOT_SET',
            answer: str = 'ANSWER_NOT_SET'
        ) -> None:
        self.prompt_text = prompt_text # prompt_image planned for later
        "Text portion of the question"
        self.answer = answer
        "The question's answer"

    def eval(self, answer: str) -> bool:
        "Evaluate an answer, returning True if correct"


class TextQuestion(Question):
    """A singular (not multiple choice) question which 
    the user answes with one line of arbitrary characters"""
    def __init__(
            self,
            prompt_text: str = 'TEXT_PROMPT_NOT_SET',
            answer: str = 'ANSWER_NOT_SET',
            case_sensitive: bool = False
        ) -> None:
        self.case_sensitive = case_sensitive
        "Whether answers should be evaluated with case sensitivity"
        if not case_sensitive:
            answer = answer.lower()
        super().__init__(prompt_text, answer)

    def eval(self, answer: str) -> bool:
        if not self.case_sensitive:
            answer = answer.lower()
        return answer == self.answer
