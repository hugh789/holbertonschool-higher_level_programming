#!/usr/bin/python3

class MyList(list):
    """A subclass of list with a print_sorted method."""

    def print_sorted(self):
        """Prints list sorted in ascending order."""
        print(sorted(self))
