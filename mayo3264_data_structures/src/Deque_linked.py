"""
-------------------------------------------------------
Linked version of the Deque ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-02-18"
-------------------------------------------------------
"""
# Imports
from copy import deepcopy


class _Deque_Node:

    def __init__(self, value, _prev, _next):
        """
        -------------------------------------------------------
        Initializes a deque node.
        Use: node = _Deque_Node(value, _prev, _next)
        -------------------------------------------------------
        Parameters:
            value - value value for node (?)
            _prev - another deque node (_Deque_Node)
            _next - another deque node (_Deque_Node)
        Returns:
            a new _Deque_Node object (_Deque_Node)

        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._prev = _prev
        self._next = _next


class Deque:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty deque.
        Use: d = deque()
        -------------------------------------------------------
        Returns:
            a new Deque object (Deque)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the deque is empty.
        Use: b = deque.is_empty()
        -------------------------------------------------------
        Returns:
            True if the deque is empty, False otherwise.
        -------------------------------------------------------
        """
        return True if self._front is None else False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of the deque.
        Use: n = len(deque)
        -------------------------------------------------------
        Returns:
            the number of values in the deque (int)
        -------------------------------------------------------
        """
        return self._count

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Deques are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a deque (Deque)
        Returns:
            equals - True if source contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        curr1 = self._front
        curr2 = target._front
        equals = True
        if self._count != target._count:
            equals = False
        else:
            while curr1 is not None and curr2 is not None:
                if curr1._value != curr2._value:
                    equals = False

                curr1 = curr1._next
                curr2 = curr2._next

        return equals

    def insert_front(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the front of the deque.
        Use: deque.insert_front(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Deque_Node(value, None, None)
        if self._front is None:
            self._front = new_node
            self._rear = new_node

        else:
            new_node._next = self._front
            self._front._prev = new_node
            self._front = new_node

        self._count += 1
        return

    def insert_rear(self, value):
        """
        -------------------------------------------------------
        Inserts a copy of value into the rear of the deque.
        Use: deque.insert_rear(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Deque_Node(value, None, None)

        if self._front is None:
            self._front = new_node
            self._rear = new_node
        else:
            self._rear._next = new_node
            new_node._prev = self._rear
            self._rear = new_node

        self._count += 1
        return

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes and returns value from the front of the deque.
        Use: v = deque.remove_front()
        -------------------------------------------------------
        Returns:
            value - the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty deque"

        value = self._front._value

        if self._count == 1:
            self._front = None
            self._rear = None

        else:
            self._front = self._front._next
            self._front._prev = None

        self._count -= 1
        return value

    def remove_rear(self):
        """
        -------------------------------------------------------
        Removes and returns value from the rear of the deque.
        Use: v = deque.remove_rear()
        -------------------------------------------------------
        Returns:
            value - the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot remove from an empty deque"

        value = self._rear._value

        if self._count == 1:
            self._front = None
            self._rear = None

        else:
            self._rear = self._rear._prev
            self._rear._next = None

        self._count -= 1
        return value

    def peek_front(self):
        """
        -------------------------------------------------------
        Peeks at the front of deque.
        Use: v = deque.peek_front()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of deque (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._front._value)
        return value

    def peek_rear(self):
        """
        -------------------------------------------------------
        Peeks at the rear of deque.
        Use: v = deque.peek_rear()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the rear of deque (?)
        -------------------------------------------------------
        """
        assert self._rear is not None, "Cannot peek at an empty deque"

        value = deepcopy(self._rear._value)

        return value

    def _swap(self, l, r):
        """
        -------------------------------------------------------
        Swaps two nodes within a deque. l has taken the place of r, 
        r has taken the place of l and _front and _rear are updated 
        as appropriate. Data is not moved.
        Use: self._swap(self, l, r):
        -------------------------------------------------------
        Parameters:
            l - a pointer to a deque node (_Deque_Node)
            r - a pointer to a deque node (_Deque_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        assert l is not None and r is not None, "nodes to swap cannot be None"

        if l == r:
            self._front = self._front

        # there are only 2 nodes
        elif self._count == 2:
            r._next = l
            l._prev = r

            l._next = None
            r._prev = None

            self._front = r
            self._rear = l
            self._rear._prev._next = l

        # l and r are front and rear
        elif l == self._front and r == self._rear:

            right_prev = r._prev
            left_next = l._next

            l._next = None
            l._prev = right_prev
            right_prev._next = l
            r._prev = None
            r._next = left_next
            left_next._prev = r

            self._front = r
            self._rear = l

        elif l == self._rear and l._prev != r:
            right_prev = r._prev
            right_next = r._next
            left_prev = l._prev

            right_prev._next = l
            left_prev._next = r

            r._next = None
            r._prev = left_prev
            self._rear = r

            l._prev = right_prev
            l._next = right_next

        # l and r adjacent and neither is front or rear
        elif l._next == r and r != self._rear and l != self._front:
            l._prev._next = r
            r._next._prev = l

            l._next = r._next
            r._prev = l._prev

            r._next = l
            l._prev = r

        # l and r not adjacent and neither is front or rear
        elif l._next != r and r != self._rear and l != self._front:
            left_prev = l._prev
            left_next = l._next

            l._next._prev = r
            l._prev._next = r
            l._next = r._next
            l._prev = r._prev

            r._prev._next = l
            r._next._prev = l
            r._next = left_next
            r._prev = left_prev

        # l and r not adjacent but l is front
        elif l == self._front and l._next != r:
            right_next = r._next
            right_prev = r._prev
            r._next = self._front._next
            r._prev = None

            l._next = right_next
            l._prev = right_prev

            right_next._prev = l
            right_prev._next = l

            self._front = r

        # l and r adjacent but l is front
        elif l == self._front and l._next == r:
            right_next = r._next
            right_prev = r._prev

            r._next._prev = l

            r._next = l
            r._prev = None
            self._front = r

            l._next = right_next
            l._prev = r

        # l and r adjacent but r is rear
        elif r == self._rear and self._rear._prev == l:
            left_prev = l._prev

            r._prev = l._prev
            r._next = l
            left_prev._next = r

            l._next = None
            l._prev = r

            self._rear = l

        # l and r not adjacent but r is rear
        elif r == self._rear and self._rear._prev != l:
            left_prev = l._prev
            left_next = l._next
            right_prev = r._prev

            left_prev._next = r
            right_prev._next = l

            l._next = None
            l._prev = right_prev

            r._prev = left_prev
            r._next = left_next

        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the deque
        from front to rear.
        Use: for v in d:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the deque (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next
