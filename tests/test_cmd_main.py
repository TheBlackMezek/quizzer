import unittest
import sys
from io import StringIO
from quizzer.interface.cmd_main import CmdMain
from quizzer.quizzes.quiz import Quiz
import quizzer.quizzes.quiz_manager as quiz_manager


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
