"Module containing loading, saving, and storagr for quizzes"
from quizzer.quizzes.quiz import Quiz
import pickle


_quizzes = {}
"Dict of all loaded quizzes"


_pickle_path = 'quizzes.pickle'
"Path which all local quizzes are saved to"


def add_quiz(quiz: Quiz) -> None:
    "Register a new quiz"
    # An exception should be thrown here if a quiz with that title already
    # exists, but idk how to do that yet
    if not quiz_exists(quiz.title):
        _quizzes[quiz.title] = quiz


def delete_quiz(quiz_name: str) -> None:
    "Delete a loaded quiz"
    # Maybe an exception should be thrown here if a quiz with that title
    # already exists
    if quiz_exists(quiz_name):
        _quizzes.pop(quiz_name)


def clear_quizzes() -> None:
    """Deletes all quizzes\n
    Do NOT use without good reason"""
    keys = list(_quizzes.keys())
    for key in keys:
        _quizzes.pop(key)


def quiz_exists(quiz_name: str) -> bool:
    "Returns whether or not a quiz with quiz_name exists"
    return quiz_name in _quizzes.keys()


def get_quiz(quiz_name: str) -> Quiz:
    "Returns a quiz with title quiz_name, or None if one doesn't exist"
    if quiz_exists(quiz_name):
        return _quizzes[quiz_name]
    else:
        return None


def load_quizzes() -> None:
    "Loads quizzes from pickle storage file"
    file = open(_pickle_path, 'rb')
    global _quizzes
    _quizzes = pickle.load(file)
    file.close()


def save_quizzes() -> None:
    "Saves quizzes to pickle file"
    file = open(_pickle_path, 'wb')
    pickle.dump(_quizzes, file)
    file.close()


def load_external_quiz(quiz_path: str) -> None:
    "Loads a new quiz from an exported file"
    print("This feature has not been implemented")


def export_quiz(quiz: Quiz) -> None:
    "Saves a quiz to a shareable file"
    print("This feature has not been implemented")
