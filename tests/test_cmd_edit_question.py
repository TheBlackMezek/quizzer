from quizzer.interface.cmd_edit_question import CmdEditQuestion
from quizzer.quizzes.questions import TextQuestion
import unittest
import sys
from io import StringIO


class Test_CmdEditQuestion(unittest.TestCase):
    # Tests for interface printing still need to be written
    def test_set_answer(self):
        "Does the editor understand how to use a new question answer?"
        cmd = CmdEditQuestion(TextQuestion())
        cmd.onecmd('answer Forty Two')
        self.assertEqual('Forty Two', cmd._new_answer)

    def test_set_text_prompt(self):
        "Does the editor understand how to use a new question prompt?"
        cmd = CmdEditQuestion(TextQuestion())
        cmd.onecmd('question What is the answer')
        self.assertEqual('What is the answer', cmd._new_text_prompt)

    def test_set_case_sensitive_true(self):
        "Does the editor understand true case sensitivity?"
        cmd = CmdEditQuestion(TextQuestion())
        cmd.onecmd('case_sensitive tRuE')
        self.assertTrue(cmd._new_case_sensitivity)

    def test_set_case_sensitive_false(self):
        "Does the editor understand false case sensitivity?"
        cmd = CmdEditQuestion(TextQuestion())
        cmd.onecmd('case_sensitive fAlSe')
        self.assertFalse(cmd._new_case_sensitivity)

    def test_set_case_sensitive_bad(self):
        "Does the editor print an error if you give it bad case sensitivity?"
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        cmd = CmdEditQuestion(TextQuestion())
        cmd.onecmd('case_sensitive invalid words')
        sys.stdout = sys.__stdout__
        expected = "Case sensitivity must be \"true\" or \"false\"\n"
        self.assertEqual(expected, capturedOutput.getvalue())
    
    def test_save_case_sensitive(self):
        "Does the editor save all data properly when case sensitive?"
        cmd = CmdEditQuestion(TextQuestion(case_sensitive=True))
        cmd.onecmd('answer New Answer')
        cmd.onecmd('question New Question')
        cmd.onecmd('save')
        self.assertEqual('New Answer', cmd._question.answer)
        self.assertEqual('New Question', cmd._question.prompt_text)
    
    def test_save_case_insensitive(self):
        "Does the editor save all data properly when case insensitive?"
        cmd = CmdEditQuestion(TextQuestion(case_sensitive=False))
        cmd.onecmd('answer New Answer')
        cmd.onecmd('question New Question')
        cmd.onecmd('save')
        self.assertEqual('new answer', cmd._question.answer)
        self.assertEqual('new question', cmd._question.prompt_text)
    
    def test_default_intro(self):
        "Is the intro set correctly when the object is created?"
        q = TextQuestion('The prompt', 'the answer', case_sensitive=False)
        cmd = CmdEditQuestion(q)
        expected = (
            "-- Editing question --\n"
            'Text prompt: "The prompt"\n'
            'Answer: "the answer"\n'
            'Case sensitive: false\n'
        )
        self.assertEqual(expected, cmd.intro)
    
    def test_intro_answer_change(self):
        "Is the answer marked as changed when a new answer is given?"
        q = TextQuestion('The prompt', 'the answer', case_sensitive=False)
        cmd = CmdEditQuestion(q)
        cmd.onecmd("answer The New Answer")
        cmd.set_intro() # called manually because onecmd() doesn't do it
        expected = (
            "-- Editing question --\n"
            'Text prompt: "The prompt"\n'
            'Answer: *"the new answer"\n'
            'Case sensitive: false\n'
        )
        self.assertEqual(expected, cmd.intro)
    
    def test_intro_case_change(self):
        "Is the case sensitivity marked as changed when a new vale is given?"
        q = TextQuestion('The prompt', 'the answer', case_sensitive=False)
        cmd = CmdEditQuestion(q)
        cmd.onecmd("answer The Answer") # to see if it prints capitals
        cmd.onecmd("case_sensitive true")
        cmd.set_intro() # called manually because onecmd() doesn't do it
        expected = (
            "-- Editing question --\n"
            'Text prompt: "The prompt"\n'
            'Answer: *"The Answer"\n'
            'Case sensitive: *true\n'
        )
        self.assertEqual(expected, cmd.intro)
