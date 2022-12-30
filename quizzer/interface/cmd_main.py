"Module containing the main menu command line class"
import cmd


class CmdMain(cmd.Cmd):
    "Quiz program main menu"
    intro="Quizzer main menu. Enter 'help' for a list of commands.\n"
    prompt='(main_menu)'

    # help, handled automatically by Cmd class

    # list quizzes

    # edit quiz

    # start quiz

    # logout (when users are implemented)

    def precmd(self, line: str) -> str:
        # For simplicity, inputs are converted to lower case
        line = line.lower()
        return line
