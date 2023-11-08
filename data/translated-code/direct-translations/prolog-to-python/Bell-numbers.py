```python
def bell(N, Bell):
    bell_helper(N, Bell, [], [])

def bell_helper(N, Bell, B, Row):
    if N == 0:
        Bell.append([1])
        return
    else:
        N1 = N - 1
        bell_helper(N1, Bell, [Row] + B, [1])
        next_row(Row, Bell[-1])

def next_row(Last, Bell1):
    if Bell1[-1][-1] == Last:
        next_row1(Last, Bell1[-1], Bell1)

def next_row1(X, Y, Bell):
    if not Y:
        return
    else:
        Y[0] = X + Y[0]
        next_row1(Y[0], Y[1:], Bell[1:])

def print_bell_numbers(Bell, N):
    if N == 0:
        return
    else:
        print(Bell[N-1][0])
        print_bell_numbers(Bell, N-1)

def print_bell_rows(Rows, N):
    if N == 0:
        return
    else:
        print_bell_row(Rows[0])
        print_bell_rows(Rows[1:], N-1)

def print_bell_row(row):
    if len(row) == 1:
        print(row[0])
    else:
        print(row[0], end=" ")
        print_bell_row(row[1:])

def main():
    Bell = []
    bell(49, Bell)
    print('First 15 Bell numbers:')
    print_bell_numbers(Bell, 15)
    print('50th Bell number:', Bell[-1][0])
    print('First 10 rows of Bell triangle:')
    print_bell_rows(Bell, 10)

main()
```