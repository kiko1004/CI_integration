from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return "Empty Stack"

    def max(self):
        try:
            return max(self.stack)
        except ValueError:
            return None
    def push(self, value):
        self.stack.append(value)


