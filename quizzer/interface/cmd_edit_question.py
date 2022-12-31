"Module containing the Cmd class for editing questions"
from cmd import Cmd
from quizzes.questions import TextQuestion


class CmdEditQuestion(Cmd):
    "Question editor interface"
    intro=""
    prompt='PROMPT_NOT_SET'

    def __init__(
            self,
            question: TextQuestion,
            completekey='tab',
            stdin=None,
            stdout=None) -> None:
        self._question = question
        "The question this interface is being used to edit"
        self._new_text_prompt = None
        "The new text prompt to be saved or discarded"
        self._new_answer = None
        "The new answer to be saved or discarded"
        self._new_case_sensitivity = question.case_sensitive
        "What case sensitivity will be saved to the question"

        self.set_prompt()
        super().__init__(completekey, stdin, stdout)

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
    
    def set_prompt(self) -> None:
        "Create a prompt string based on question settings"
        self.prompt = "\n-- Editing question --\n"

        if self._new_text_prompt is not None:
            text_prompt = f'*"{self._new_text_prompt}"'
        else:
            text_prompt = f'"{self._question.prompt_text}"'

        if self._new_answer is not None:
            answer = f'*"{self._new_answer}"'
        else:
            answer = f'"{self._question.answer}"'

        if self._new_case_sensitivity:
            case_sensitive = 'true'
        else:
            case_sensitive = 'false'
            answer = answer.lower()
        if self._new_case_sensitivity is not self._question.case_sensitive:
            case_sensitive = '*'+case_sensitive
        
        self.prompt += f"Text prompt: {text_prompt}\n"
        self.prompt += f"Answer: {answer}\n"
        self.prompt += f"Case sensitive: {case_sensitive}\n"
        self.prompt += "\n(edit_question) "
    
    def postcmd(self, stop: bool, line: str) -> bool:
        # This does not seem to get called by onecmd()
        self.set_prompt()
        return super().postcmd(stop, line)
