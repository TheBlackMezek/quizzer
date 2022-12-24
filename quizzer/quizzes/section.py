"Module containing the Section class for quizzes"
import random
from copy import copy


class Section:
    "Class for storing and sorting questions"
    def __init__(self) -> None:
        self.title = 'SECTION_TITLE_NOT_SET'
        "Name of the section to be displayed during quiz creation"
        self.elements = []
        "A list of Questions and Sections which comprise this Section"
        self.randomize = False
        "If true, will shuffle self.elements on __iter__()"

        self._iter_elements = None
        "The sequence of elements used for the iterator"
        self._element_idx = 0
        "The index of the __next__ iterator element"
        self._element_iter = None
        "Storage for the iterator if the current element is a Section"


    def __iter__(self):
        self._iter_elements = copy(self.elements)
        if self.randomize:
            random.shuffle(self._iter_elements)
        self._element_idx = 0
        # We don't need to set self._element_iter because it should be None
        return self

    def __next__(self):
        if self._element_idx < len(self.elements):
            if self._element_iter is not None:
                try:
                    return self._element_iter.__next__()
                except StopIteration:
                    self._element_iter = None
            if self._element_iter is None:
                ret = self._iter_elements[self._element_idx]
                self._element_idx += 1
                if type(ret) is Section:
                    self._element_iter = ret.__iter__()
                    ret = self._element_iter.__next__()
            return ret
        else:
            # The list isn't in use anymore so might as well delete it
            self._iter_elements = None
            raise StopIteration
