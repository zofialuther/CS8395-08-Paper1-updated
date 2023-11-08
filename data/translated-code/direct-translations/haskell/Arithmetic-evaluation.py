from typing import Union
import re

class Exp:
    def __init__(self, op: str, left: Union[int, 'Exp'], right: Union[int, 'Exp']):
        self.op = op
        self.left = left
        self.right = right

def parse_expr(s: str) -> Exp:
    def factor() -> Exp:
        nonlocal s
        match = re.match(r'^\((.*)\)$', s)
        if match:
            s = match.group(1)
            return parse_expr(s)
        else:
            match = re.match(r'^(\d+)', s)
            if match:
                num = int(match.group(1))
                s = s[len(match.group(0)):]
                return num
            else:
                raise ValueError('Invalid expression')

    def apply_op(left: Exp, op: str, right: Exp) -> Exp:
        if op == '+':
            return Exp('Add', left, right)
        elif op == '-':
            return Exp('Sub', left, right)
        elif op == '*':
            return Exp('Mul', left, right)
        elif op == '/':
            return Exp('Div', left, right)
        else:
            raise ValueError('Invalid operator')

    def parse_table(table: list, i: int) -> Exp:
        if i == len(table):
            return factor()
        else:
            left = parse_table(table, i + 1)
            while i < len(table[i]) and s.startswith(table[i][0]):
                op = table[i][0]
                s = s[len(op):]
                right = parse_table(table, i + 1)
                left = apply_op(left, op, right)
            return left

    s = s.replace(' ', '')
    table = [['*', '/'], ['+', '-']]
    return parse_table(table, 0)

def eval_expr(exp: Exp) -> int:
    if isinstance(exp, int):
        return exp
    else:
        if exp.op == 'Add':
            return eval_expr(exp.left) + eval_expr(exp.right)
        elif exp.op == 'Sub':
            return eval_expr(exp.left) - eval_expr(exp.right)
        elif exp.op == 'Mul':
            return eval_expr(exp.left) * eval_expr(exp.right)
        elif exp.op == 'Div':
            return eval_expr(exp.left) // eval_expr(exp.right)

def solution(s: str) -> int:
    exp = parse_expr(s)
    return eval_expr(exp)

print(solution("(1+3)*7"))