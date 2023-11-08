```python
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
        in_lit = [False] * len(lit)
        stack = []
        for i in range(len(expr)):
            c = expr[i]
            x = 0
            if any(in_lit):
                x = in_lit.index(True)
                if c == lit[x] and expr[i-1] != esc[x]:
                    in_lit[x] = False
            elif c in lit:
                in_lit[lit.index(c)] = True
            elif c in obr:
                stack.append(cbr[obr.index(c)])
            elif c in cbr:
                if not stack or stack.pop() != c:
                    return False
            elif not other:
                return False
        return not stack
    
    @staticmethod
    def main(args):
        print("With areSquareBracketsBalanced:")
        for s in ["", "[]", "[][]", "[[][]]", "][", "][][", "[]][[]", "[", "]"]:
            print(f"{s}: {BalancedBrackets.areSquareBracketsBalanced(s)}")
        
        print("\nBut also with areStringAndBracketsBalanced:")
        for s in ["x[]", "[x]", "[]x", "([{}])", "([{}]()", "([{ '([{\\'([{' \"([{\\\"([{\" }])"]:
            print(f"{s}: {BalancedBrackets.areStringAndBracketsBalanced(s)}")

BalancedBrackets.main([])
```