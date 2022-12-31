"Module containing the Cmd class for editing questions"
from cmd import Cmd
from quizzer.quizzes.questions import TextQuestion, Question


class CmdEditQuestion(Cmd):
    "Question editor interface"
    intro="Quizzer main menu. Enter 'help' for a list of commands.\n"
    prompt='(edit_question)'

    def __init__(
            self,
            question: TextQuestion,
            completekey='tab',
            stdin=None,
            stdout=None) -> None:
        super().__init__(completekey, stdin, stdout)
        self._question = question
        "The question this interface is being used to edit"
        self._new_text_prompt = None
        "The new text prompt to be saved or discarded"
        self._new_answer = None
        "The new answer to be saved or discarded"
        self._new_case_sensitivity = question.case_sensitive

    def do_question(self, arg):
        "Set a new text prompt for the question"
        # Stored without case sensitivity, will be lower()ed if saved
        self._new_text_prompt = arg

    def do_answer(self, arg):
        "Set a new answer for the question"
        # Stored without case sensitivity, will be lower()ed if saved
        self._new_answer = arg

    def do_case_sensitive(self, arg):
        "Set case sensitivity to \"true\" or \"false\""
        if arg.lower() == 'true':
            self._new_case_sensitivity = True
        elif arg.lower() == 'false':
            self._new_case_sensitivity = False
        else:
            print("Case sensitivity must be \"true\" or \"false\"")

    def do_save(self, arg):
        """Save all changes made to this question and return to section
        (changes not saved to file until whole quiz saved)"""
        if self._new_text_prompt is not None:
            if not self._new_case_sensitivity:
                self._new_text_prompt = self._new_text_prompt.lower()
            self._question.prompt_text = self._new_text_prompt
        if self._new_answer is not None:
            if not self._new_case_sensitivity:
                self._new_answer = self._new_answer.lower()
            self._question.answer = self._new_answer
        self._question.case_sensitive = self._new_case_sensitivity
        return True

    def do_discard(self, arg):
        "Discard all changes made to this question and return to section"
        return True

    def precmd(self, line: str) -> str:
        # For simplicity, inputs are converted to lower case
        line = line.lower()
        return line
