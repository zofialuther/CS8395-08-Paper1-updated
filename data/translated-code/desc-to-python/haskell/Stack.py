```python
class State:
    def __init__(self, state_function):
        self.state_function = state_function

    def run_state(self, initial_state):
        return self.state_function(initial_state)

class Stack:
    @staticmethod
    def push(element):
        return State(lambda stack: (None, [element] + stack))

    @staticmethod
    def pop():
        return State(lambda stack: (stack[0], stack[1:]))

    @staticmethod
    def empty():
        return State(lambda stack: (stack == [], stack))

    @staticmethod
    def peek():
        return State(lambda stack: (stack[0], stack))

    @staticmethod
    def nonEmpty():
        return State(lambda stack: (stack != [], stack))
```