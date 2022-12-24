"Module containing the Quiz class"


class Quiz:
    "Class for storing questions, processing answers, and tracking status"
    def __init__(self) -> None:
        self.title = 'QUIZ_TITLE_NOT_SET'
        "Title of the quiz to be displayed to the user"
        self._sections = [] # This needs to contain a root section
        "Each section can contain subsections and questions"
