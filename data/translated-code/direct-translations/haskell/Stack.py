from typing import TypeVar, List
from dataclasses import dataclass
import functools

T = TypeVar('T')
S = TypeVar('S')


@dataclass
class State:
    value: List[T]

    def push(self, item: T) -> 'State':
        self.value.append(item)
        return self

    def pop(self) -> T:
        if not self.value:
            raise ValueError("Stack empty")
        return self.value.pop()

    def empty(self) -> bool:
        return not self.value

    def peek(self) -> T:
        if not self.value:
            raise ValueError("Stack empty")
        return self.value[-1]


def stack_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if not self.value:
            raise ValueError("Stack empty")
        return func(self, *args, **kwargs)
    return wrapper


State.push = stack_decorator(State.push)
State.pop = stack_decorator(State.pop)
State.empty = stack_decorator(State.empty)
State.peek = stack_decorator(State.peek)


# Example usage
stack = State([])
print(stack.empty())  # True
stack = stack.push(1).push(2).push(3)
print(stack.peek())  # 3
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.empty())  # True