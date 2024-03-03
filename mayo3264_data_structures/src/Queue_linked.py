"""
-------------------------------------------------------
Linked version of the Queue ADT.
-------------------------------------------------------
Author:  David Brown
ID:      123456789
Email:   dbrown@wlu.ca
__updated__ = "2024-02-17"
-------------------------------------------------------
"""
from copy import deepcopy


class _Queue_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a queue node that contains a copy of value
        and a link to the next node in the queue.
        Use: node = _Queue_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            value - value for node (?)
            next_ - another Queue node (_Queue_Node)
        Returns:
            a new _Queue_Node object (_Queue_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class Queue:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty queue. Data is stored in a Python list.
        Use: queue = Queue()
        -------------------------------------------------------
        Returns:
            a new Queue object (Queue)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the queue is empty.
        Use: b = queue.is_empty()
        -------------------------------------------------------
        Returns:
            True if queue is empty, False otherwise.
        -------------------------------------------------------
        """

        return True if self._count == 0 else False

    def is_full(self):
        """
        -------------------------------------------------------
        Determines if the queue is full.
        Use: b = queue.is_full()
        -------------------------------------------------------
        Returns:
            True if queue is full, False otherwise.
        -------------------------------------------------------
        """

        return False

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the length of the queue.
        Use: n = len(queue)
        -------------------------------------------------------
        Returns:
            the number of values in queue.
        -------------------------------------------------------
        """

        return self._count

    def insert(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the rear of queue.
        Use: queue.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        new_node = _Queue_Node(value, None)

        if self._front is None:
            self._front = new_node
            self._rear = new_node

        else:
            self._rear._next = new_node
            self._rear = new_node

        self._count += 1

        return

    def remove(self):
        """
        -------------------------------------------------------
        Removes and returns value from the queue.
        Use: value = queue.remove()
        -------------------------------------------------------
        Returns:
            value - the value at the front of the queue - the value is
            removed from queue (?)
        -------------------------------------------------------        
        """
        assert self._front is not None, "Cannot remove from an empty queue"

        if self._count == 1:
            print(3)

            value = self._front._value
            self._rear = None
            self._front = self._rear

        else:
            value = self._front._value
            self._front = self._front._next

        self._count -= 1
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the front of queue.
        Use: value = queue.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the value at the front of queue -
            the value is not removed from queue (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty queue"

        value = deepcopy(self._front._value)

        return value

    def _move_front_to_rear(self, source):
        """
        -------------------------------------------------------
        Moves the front node from the source queue to the rear of the target queue.
        The target queue contains the old front node of the source queue.
        The source queue front is updated.
        Use: target._move_front_to_rear(source)
        -------------------------------------------------------
        Parameters:
            source - a linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot move the front of an empty queue"

        temp = source._front
        source._front = source._front._next

        if source._front is None:
            source._rear = None

        if self._front is None:
            temp._next = self._front
            self._front = temp
            self._rear = temp

        else:
            temp._next = None
            self._rear._next = temp
            self._rear = temp

        self._count += 1
        source._count -= 1

        return

    def _append_queue(self, source):
        """
        -------------------------------------------------------
        Appends the entire source queue to the rear of the target queue.
        The source queue becomes empty.
        Use: target._append_queue(source)
        -------------------------------------------------------
        Parameters:
            source - an linked-based queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """
        assert source._front is not None, "Cannot append an empty queue"
        temp = source._front
        temp_rear = source._rear

        if self._front is None:
            self._front = temp
            self._rear = temp_rear
        else:
            self._rear._next = temp
            self._rear = temp_rear

        source._front = None
        source._rear = None
        self._count += source._count
        source._count = 0
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source queues into the current target queue. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an linked queue (Queue)
            source2 - an linked queue (Queue)
        Returns:
            None
        -------------------------------------------------------
        """

        if source1._front is None and source2._front is None:
            self._front = None
        elif source1._front is None:
            self._append_queue(source2)

        elif source2._front is None:
            self._append_queue(source1)

        else:

            while source1._front is not None and source2._front is not None:
                self._move_front_to_rear(source1)
                self._move_front_to_rear(source2)

            if source1._front is None and source2._front is not None:
                self._append_queue(source2)

            elif source2._front is None and source1._front is not None:
                self._append_queue(source1)

        return

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source queue into separate target queues with values 
        alternating into the targets. At finish source queue is empty.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Queue)
            target2 - contains other alternating values from source (Queue)
        -------------------------------------------------------
        """
        target1 = Queue()
        target2 = Queue()

        while self._front is not None:
            target1._move_front_to_rear(self)

            if self._front is not None:
                target2._move_front_to_rear(self)

        return target1, target2

    def __eq__(self, target):
        """
        ---------------------------------------------------------
        Determines whether two Queues are equal.
        Values in self and target are compared and if all values are equal
        and in the same order, returns True, otherwise returns False.
        Use: equals = source == target
        ---------------
        Parameters:
            target - a queue (Queue)
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
        elif self._front is None:
            equals = True

        else:
            while curr1 is not None and equals:
                if curr1._value != curr2._value:
                    equals = False
                curr1 = curr1._next
                curr2 = curr2._next

        return equals

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the queue
        from front to rear.
        Use: for v in q:
        -------------------------------------------------------
        Returns:
            value - the next value in the queue (?)
        -------------------------------------------------------
        """
        current = self._front

        while current is not None:
            yield current._value
            current = current._next

    def print(self):
        """
        -------------------------------------------------------
        Prints the contents of Queue from front to rear.
        Use: q.print()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        curr = self._front

        while curr is not None:
            print(curr._value)
            curr = curr._next
        return
