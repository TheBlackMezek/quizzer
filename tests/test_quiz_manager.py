from quizzer.quizzes.quiz_manager import (
    _quizzes,
    _pickle_path,
    add_quiz,
    delete_quiz,
    quiz_exists,
    get_quiz,
    save_quizzes,
    load_quizzes,
    clear_quizzes
)
from quizzer.quizzes.quiz import Quiz
from quizzer.quizzes.section import Section
import unittest
import pickle
import os


class Test_QuizManager(unittest.TestCase):
    def test_clear_quizzes(self):
        "Does clear_quizzes actually delete all quizzes?"
        _quizzes['quiz_1'] = Quiz()
        _quizzes['quiz_2'] = Quiz()

        clear_quizzes()
        self.assertEqual(0, len(_quizzes))


    def test_add_quiz(self):
        """Are new quizzes correctly added to the dict?"""
        quiz = Quiz()
        quiz.title = 'quiz_title'
        add_quiz(quiz)
        self.assertTrue('quiz_title' in _quizzes.keys())
        clear_quizzes()

    def test_delete_quiz(self):
        """Are new quizzes correctly deleted from the dict?"""
        quiz = Quiz()
        quiz.title = 'quiz_title'
        add_quiz(quiz)
        delete_quiz('quiz_title')
        self.assertFalse('quiz_title' in _quizzes.keys())

    def test_quiz_exists_true(self):
        """Does quiz_exists detect when a quiz exists?"""
        quiz = Quiz()
        quiz.title = 'quiz_title'
        add_quiz(quiz)
        self.assertTrue(quiz_exists('quiz_title'))
        clear_quizzes()

    def test_quiz_exists_false(self):
        """Does quiz_exists detect when a quiz doesn't exist?"""
        self.assertFalse(quiz_exists('quiz_title'))
    
    def test_get_quiz_exists(self):
        "Will get_quiz return the named quiz if it exists?"
        for i in range(3):
            quiz = Quiz()
            quiz.title = f'quiz_{i}'
            add_quiz(quiz)
        returned = get_quiz('quiz_1')
        self.assertEqual('quiz_1', returned.title)
        clear_quizzes()
    
    def test_get_quiz_nonexistant(self):
        "Will get_quiz return None if the named quiz doesn't exist?"
        for i in range(3):
            quiz = Quiz()
            quiz.title = f'quiz_{i}'
            add_quiz(quiz)
        returned = get_quiz('quiz_5')
        self.assertEqual(None, returned)
        clear_quizzes()

    def test_save_quizzes(self):
        "Are quizzes pickled?"
        q1 = Quiz()
        q1.title = 'quiz_1'
        add_quiz(q1)

        save_quizzes()

        file = open(_pickle_path, 'rb')
        quizzes = pickle.load(file)
        file.close()
        os.remove(_pickle_path)

        self.assertTrue('quiz_1' in quizzes.keys())
        clear_quizzes()
    
    def test_save_sections(self):
        "Are sections within quizzes pickled?"
        global _quizzes
        print(len(_quizzes.keys()))
        q1 = Quiz()
        q1.title = 'quiz_1'
        section = Section()
        section.title = 'section_1'
        q1._root_section.elements.append(section)
        print(len(q1._root_section.elements))
        add_quiz(q1)

        save_quizzes()

        file = open(_pickle_path, 'rb')
        quizzes = pickle.load(file)
        file.close()
        os.remove(_pickle_path)

        quiz = quizzes['quiz_1']
        root = quiz._root_section
        print(len(root.elements))
        sec = root.elements[0]
        self.assertEqual('section_1', sec.title)
        clear_quizzes()
    
    def test_load_quizzes(self):
        "Are pickled quizzes loaded?"
        q1 = Quiz()
        q1.title = 'quiz_1'
        quizzes = {
            'quiz_1': q1
        }
        file = open(_pickle_path, 'wb')
        pickle.dump(quizzes, file)
        file.close()

        load_quizzes()

        os.remove(_pickle_path)

        self.assertTrue(quiz_exists('quiz_1'))
        clear_quizzes()
