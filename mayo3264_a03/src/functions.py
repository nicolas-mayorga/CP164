"""
-------------------------------------------------------
Assignment 3 Functions
-------------------------------------------------------
Author:  Nicolas Mayorga
ID:      169053264
Email:   mayo3264@mylaurier.ca
__updated__ = "2024-01-28"
-------------------------------------------------------
"""
from Stack_array import Stack
from copy import deepcopy


def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()

    while not source1.is_empty() and not source2.is_empty():
        target.push(source1.pop())
        target.push(source2.pop())

    if source1.is_empty():
        for item in source2:
            target.push(item)
            source2.pop()

    elif source2.is_empty():
        for item in source1:
            target.push(item)
            source1.pop()

    return target


def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """
    list = []
    i = 0
    while not source.is_empty():
        list.append(source.pop())
        i += 1
    j = 0
    while i > 0:
        source.push(list[j])
        j += 1
        i -= 1
    return


def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    stack = Stack()
    new_string = ''
    palindrome = False
    old_string = ''
    for char in string:
        if char.isalpha():
            stack.push(char)
            old_string += char

    for item in stack:
        new_string += item

    if new_string.lower() == old_string.lower():
        palindrome = True

    return palindrome


# Constants
OPERATORS = "+-*/"


def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    stack = Stack()
    answer = 0
    for char in string.split(' '):
        if char.isdigit():
            stack.push(char)
        elif char in OPERATORS:
            if char == '+':
                value1 = float(stack.pop())
                value2 = float(stack.pop())
                value = value2 + value1
                stack.push(value)

            elif char == '*':
                value1 = float(stack.pop())
                value2 = float(stack.pop())
                value = value2 * value1
                stack.push(value)

            elif char == '-':
                value1 = float(stack.pop())
                value2 = float(stack.pop())
                value = value2 - value1
                stack.push(value)

            elif char == '/':
                value1 = float(stack.pop())
                value2 = float(stack.pop())
                if value1 == 0:
                    answer = None
                    break
                else:
                    value = value2 / value1
                stack.push(value)
    if answer != None:
        answer = stack.pop()
    return answer


def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """

    path = None
    stack = Stack()
    for key in maze:
        if 'X' in maze[key]:
            path = []
    if path == []:
        for key in maze:
            if 'X' in maze[key]:
                path.append('X')
                break

            if len(maze[key]) != 0:
                for branch in maze[key]:
                    stack.push(branch)

                if len(maze[stack.peek()]) != 0:
                    path.append(stack.pop())

    return path
