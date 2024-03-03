"""
-------------------------------------------------------
Array version of the Stack ADT.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 A
__updated__ = "2024-01-20"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an is_empty stack. Data is stored in a Python list.
        Use: s = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the stack is empty.
        Use: b = s.is_empty()
        -------------------------------------------------------
        Returns:
            True if the stack is empty, False otherwise
        -------------------------------------------------------
        """
        empty = True
        if len(self._values) != 0:
            empty = False
        return empty

    def push(self, value):
        """
        -------------------------------------------------------
        Pushes a copy of value onto the top of the stack.
        Use: s.push(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

    def pop(self):
        """
        -------------------------------------------------------
        Pops and returns the top of stack. The value is removed
        from the stack. Attempting to pop from an empty stack
        throws an exception.
        Use: value = s.pop()
        -------------------------------------------------------
        Returns:
            value - the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty stack"
        value = self._values[-1]
        self._values.pop(len(self._values) - 1)

        return value

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the value at the top of the stack.
        Attempting to peek at an empty stack throws an exception.
        Use: value = s.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the top of the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        value = deepcopy(self._values[-1])
        return value

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        i = len(source1._values) - 1
        j = len(source2._values) - 1
        while len(source1._values) > 0 and len(source2._values) > 0:
            self._values.append(source1._values[i])
            self._values.append(source2._values[j])
            source1._values.pop(i)
            source2._values.pop(j)

            i -= 1
            j -= 1

        if len(source1._values) == 0:
            for i in range(len(source2._values) - 1, -1, -1):
                self._values.append(source2._values[i])
                source2._values.pop(i)

        elif len(source2._values) == 0:
            for i in range(len(source1._values) - 1, -1, -1):
                self._values.append(source1._values[i])
                source1._values.pop(i)
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        lst = []
        i = len(self._values) - 1

        while i > -1:
            lst.append(self._values[i])
            self._values.pop(i)
            i -= 1

        for i in range(len(lst)):
            self._values.append(lst[i])

        return

    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
