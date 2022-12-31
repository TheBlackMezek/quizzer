"""Module which should be run on program start; 
handles all initial calls and setup"""
from interface.cmd_main import CmdMain


#CmdMain().cmdloop()

from interface.cmd_edit_question import CmdEditQuestion
from quizzes.questions import TextQuestion
CmdEditQuestion(TextQuestion()).cmdloop()
