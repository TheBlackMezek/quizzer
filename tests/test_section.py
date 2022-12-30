import quizzer.quizzes.section as section
import quizzer.quizzes.questions as questions
import unittest


class Test_TextSection(unittest.TestCase):
    def test_non_randomized_questions(self):
        """Will a Section iterate through non randomized questions?"""
        s = section.Section()
        # randomize is False by default
        s.elements = [
            questions.Question('Q1'),
            questions.Question('Q2')
        ]
        n = 0
        for e in s:
            self.assertEqual(e, s.elements[n])
            n += 1

    def test_non_randomized_sections(self):
        """Will a Section iterate through non randomized 
        mixed questions and sections?"""
        s = section.Section()
        # randomize is False by default
        sub_s = section.Section()
        sub_s.elements = [
            questions.Question('sub_Q1'),
            questions.Question('sub_Q2')
        ]
        s.elements = [
            questions.Question('Q1'),
            sub_s
        ]
        n = 0
        for e in s:
            if n == 2:
                self.assertEqual(e, sub_s.elements[1])
            n += 1

    def test_nested_subsections(self):
        """Will subsections iterate their own subsections?"""
        subsub_s = section.Section()
        subsub_s.elements = [
            questions.Question('subsub_Q1'),
            questions.Question('subsub_Q2')
        ]
        sub_s = section.Section()
        sub_s.elements = [
            questions.Question('sub_Q1'),
            subsub_s
        ]
        s = section.Section()
        s.elements = [
            questions.Question('Q1'),
            sub_s
        ]
        n = 0
        for e in s:
            if n == 3:
                self.assertEqual(e, subsub_s.elements[1])
            n += 1
    
    def test_question_count(self):
        "Does question_count() iterate through questions and subsections?"
        sub_s = section.Section()
        sub_s.elements = [
            questions.Question('sub_Q1'),
            questions.TextQuestion('sub_Q2')
        ]
        s = section.Section()
        s.elements = [
            questions.Question('Q1'),
            sub_s
        ]
        self.assertEqual(3, s.question_count())
