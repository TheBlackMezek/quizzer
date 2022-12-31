import unittest
import sys
from io import StringIO
from interface.cmd_main import CmdMain, quiz_manager
from quizzes.quiz import Quiz


class Test_CmdMain(unittest.TestCase):
    def test_list_quizzes(self):
        "Does the 'quizzes' command print the list of quizzes?"
        q1 = Quiz()
        q1.title = 'quiz_1'
        quiz_manager.add_quiz(q1)
        q2 = Quiz()
        q2.title = 'quiz_2'
        quiz_manager.add_quiz(q2)

        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        CmdMain().onecmd('quizzes')
        sys.stdout = sys.__stdout__
        expected = (
            "Loaded quizzes:\n"
            "quiz_1\n"
            "quiz_2\n"
        )
        self.assertEqual(expected, capturedOutput.getvalue())
        quiz_manager.clear_quizzes()
