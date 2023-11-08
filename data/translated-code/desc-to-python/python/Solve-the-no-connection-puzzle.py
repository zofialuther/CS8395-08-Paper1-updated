```python
def pp(solution):
    board = """
    | {0} | {1} | {2} |
    | {3} | {4} | {5} |
    | {6} | {7} | {8} |
    """
    board = board.format(*solution)
    print(board)

solutions = [
    ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X'],
    ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']
]

for solution in solutions:
    pp(solution)
```