import quizzer.quizzes.quiz as quiz
#import quizzer.quizzes.section as section
import quizzer.quizzes.questions as questions
import unittest


class Test_Quiz(unittest.TestCase):
    def test_session_setup(self):
        """Is the first question queued when a Quiz session begins?"""
        q = quiz.Quiz()
        q._root_section.elements = [
            questions.Question('Q1'),
            questions.Question('Q2')
        ]
        q.start_session()
        self.assertEqual('Q1', q.get_prompt())
    
    def test_true_answer_submission(self):
        """Does a Quiz return the correct values when a true answer is given
        for the current question?"""
        q = quiz.Quiz()
        q._root_section.elements = [
            questions.TextQuestion('Q1', 'the answer')
        ]
        q.start_session()
        result, true_answer = q.submit_answer('the answer')
        self.assertEqual(True, result)
        self.assertEqual(true_answer, 'the answer')
    
    def test_false_answer_submission(self):
        """Does a Quiz return the correct values when a false answer is given
        for the current question?"""
        q = quiz.Quiz()
        q._root_section.elements = [
            questions.TextQuestion('Q1', 'the answer')
        ]
        q.start_session()
        result, true_answer = q.submit_answer('not the answer')
        self.assertEqual(False, result)
        self.assertEqual(true_answer, 'the answer')
    
    def test_session_ending(self):
        "Does a Quiz end its session when the last answer is submitted?"
        q = quiz.Quiz()
        q._root_section.elements = [
            questions.TextQuestion('Q1'),
            questions.TextQuestion('Q2')
        ]
        q.start_session()
        q.submit_answer("This string doesn't matter")
        q.submit_answer("This string doesn't matter")
        self.assertEqual(False, q.in_session)
