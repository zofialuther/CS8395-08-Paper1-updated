class Stack:
    def __init__(self):
        self.items = []

    def empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

stack = Stack()
print("New stack empty? " + str(stack.empty()))

stack.push("There can be only one")
print("Pushed stack empty? " + str(stack.empty()))
print("Popped single entry: " + stack.pop())

stack.push("First")
stack.push("Second")
print("Popped entry should be second: " + stack.pop())

stack.pop()
stack.pop()