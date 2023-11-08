from collections import deque

class BalancedBrackets:
    
    @staticmethod
    def areSquareBracketsBalanced(expr):
        return BalancedBrackets.isBalanced(expr, "", "", "[", "]", False)

    @staticmethod
    def areBracketsBalanced(expr):
        return BalancedBrackets.isBalanced(expr, "", "", "{([", "})]", False)

    @staticmethod
    def areStringAndBracketsBalanced(expr):
        return BalancedBrackets.isBalanced(expr, "'\"", "\\\\", "{([", "})]", True)

    @staticmethod
    def isBalanced(expr, lit, esc, obr, cbr, other):
        inLit = [False] * len(lit)
        stack = deque()

        for i in range(len(expr)):
            c = expr[i]
            x = 0

            if True in inLit:
                x = inLit.index(True)
                if c == lit[x] and expr[i-1] != esc[x]:
                    inLit[x] = False
            elif c in lit:
                x = lit.index(c)
                inLit[x] = True
            elif c in obr:
                x = obr.index(c)
                stack.append(cbr[x])
            elif c in cbr:
                if len(stack) == 0 or stack.pop() != c:
                    return False
            elif not other:
                return False

        return len(stack) == 0

    @staticmethod
    def indexOf(a, b):
        for i in range(len(a)):
            if a[i] == b:
                return i
        return -1

    @staticmethod
    def get(s, i):
        return s[i]

    @staticmethod
    def main():
        print("With areSquareBracketsBalanced:")
        for s in ["", "[]", "[][]", "[[][]]", "][", "][][", "[]][[]", "[", "]"]:
            print(f"{s}: {BalancedBrackets.areSquareBracketsBalanced(s)}")
        print("\nBut also with areStringAndBracketsBalanced:")
        for s in ["x[]", "[x]", "[]x", "([{}])", "([{}]()", "([{ '([{\\'([{' \"([{\\\"([{\" }])"]:
            print(f"{s}: {BalancedBrackets.areStringAndBracketsBalanced(s)}")

BalancedBrackets.main()