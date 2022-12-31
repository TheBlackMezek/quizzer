"Module containing the main menu command line class"
import cmd
import quizzes.quiz_manager as quiz_manager


class CmdMain(cmd.Cmd):
    "Quiz program main menu"
    intro="Quizzer main menu. Enter 'help' for a list of commands.\n"
    prompt='(main_menu)'

    # help, handled automatically by Cmd class

    def do_quizzes(self, arg):
        "Print a list of all loaded quizzes"
        print("Loaded quizzes:")
        quizzes = quiz_manager.quiz_list()
        for title in quizzes:
            print(title)

    # edit quiz

    # start quiz

    # logout (when users are implemented)

    def precmd(self, line: str) -> str:
        # For simplicity, inputs are converted to lower case
        line = line.lower()
        return line
