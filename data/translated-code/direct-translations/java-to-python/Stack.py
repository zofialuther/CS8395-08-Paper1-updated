from collections import deque

class StackTest:
    def main(self):
        stack = deque()

        print("New stack empty?", not stack)

        stack.append("There can be only one")
        print("Pushed stack empty?", not stack)
        print("Popped single entry:", stack.pop())

        stack.append("First")
        stack.append("Second")
        print("Popped entry should be second:", stack.pop())

        # Popping an empty stack will throw...
        stack.pop()
        stack.pop()

if __name__ == "__main__":
    test = StackTest()
    test.main()