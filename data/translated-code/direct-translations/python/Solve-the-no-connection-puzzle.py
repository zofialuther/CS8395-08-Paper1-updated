```python
def pp(solution):
    """Prettyprint a solution"""
    boardformat = r"""
         0   1
        /|\ /|\
       / | X | \
      /  |/ \|  \
     2 - 3 - 4 - 5
      \  |\ /|  /
       \ | X | /
        \|/ \|/
         6   7"""
    for letter, number in zip("01234567", solution):
        boardformat = boardformat.replace(letter, str(number))
    print(boardformat)


if __name__ == '__main__':
    solutions = [[0, 1, 2, 3, 4, 5, 6, 7], [7, 6, 5, 4, 3, 2, 1, 0]]  # Example solutions
    for i, s in enumerate(solutions, 1):
        print("\nSolution", i, end='')
        pp(s)
```