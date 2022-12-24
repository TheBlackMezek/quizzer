import quizzer.quizzes.questions as questions
import unittest


class Test_TextQuestion(unittest.TestCase):
    def test_class_answer_case_insensitivity(self):
        """What if an answer is passed to TextQuestion on creation 
        which has capital letters?"""
        q = questions.TextQuestion(
            answer='CORRECT ANSWER',
            case_sensitive=False
        )
        self.assertEqual(q.eval('correct answer'), True)

    def test_user_answer_case_insensitivity(self):
        """What if a case insensitive question is given an answer 
        containing uppercase characters?"""
        q = questions.TextQuestion(
            answer='correct answer',
            case_sensitive=False
        )
        self.assertEqual(q.eval('CoRrEcT aNsWeR'), True)

    def test_user_answer_case_sensitivity(self):
        """What if a case sensitive question is given an answer 
        containing wrong case characters?"""
        q = questions.TextQuestion(
            answer='Correct Answer',
            case_sensitive=True
        )
        self.assertEqual(q.eval('CoRrEcT aNsWeR'), False)
