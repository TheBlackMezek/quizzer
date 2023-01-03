"Module containing the Cmd class for editing sections"
from cmd import Cmd
from quizzes.section import Section


class CmdEditSection(Cmd):
    "Question editor interface"
    intro=""
    prompt='PROMPT_NOT_SET'

    def __init__(
            self,
            section: Section,
            section_hierarchy: list,
            root: bool = False,
            completekey='tab',
            stdin=None,
            stdout=None) -> None:
        self._section = section
        "The section this interface is being used to edit"
        self._hierarchy = section_hierarchy
        "Ordered list of parent sections"
        self._root = root
        "Is this the root section of a Quiz?"
        self._new_title = None
        "The new title to be saved or discarded"

        self.changes_made = False
        "If true, changes were made that need to be saved"
        # For edits to be discardable, the original state of the entire quiz
        # needs to be saved. Easiest way to do this is to edit copies rather
        # than the real data. When editing a subsection, pass in a copy of it
        # to the editor. If the editor marks that changes were saved, replace
        # the original with the copy.

        super().__init__(completekey, stdin, stdout)
    
    def do_title(self, arg):
        "Set the section's title"
        if self._root:
            print("Cannot change title of the root section")
            return False
        if not arg.replace(' ', '').isalnum():
            # Just in case special characters let people insert code
            print(
                "Section titles can only contain"
                " letters, numbers, and spaces"
            )
            return False
        self._new_title = arg
    
    # Edit an existing question

    # Create a new question

    # Edit an existing section

    # Create a new section

    # Move element

    # Delete element

    def do_save(self, arg):
        "Save changes"
        if self._new_title is not None:
            self._section.title = self._new_title
        self.changes_made = True
        return True

    # Discard

    # Set prompt, which should include section name & path
