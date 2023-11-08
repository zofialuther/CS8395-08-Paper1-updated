def bell(N, Bell):
    bell(N, Bell, [], _)

def bell(N, Bell, B, Row):
    if N == 0:
        return
    N1 = N - 1
    bell(N1, Bell, [Row]+B, Last)
    next_row(Row, Last)

def next_row(Row, Last):
    if not Bell:
        return
    Y = Last + Bell[0]
    next_row1(Y, Bell[1:], Bell)

def next_row1(X, Rest, Bell):
    if not Rest or not Bell:
        return
    Y = X + Bell[0]
    next_row1(Y, Rest, Bell[1:])

def print_bell_numbers(Bell, N):
    if N == 0:
        return
    print(Bell[0][0])
    N1 = N - 1
    print_bell_numbers(Bell[1:], N1)

def print_bell_rows(Bell, N):
    if N == 0:
        return
    print_bell_row(Bell[0])
    N1 = N - 1
    print_bell_rows(Bell[1:], N1)

def print_bell_row(row):
    if len(row) == 1:
        print(row[0])
    else:
        print(row[0], end=" ")
        print_bell_row(row[1:])

def main():
    Bell = []
    bell(49, Bell)
    print('First 15 Bell numbers:\n')
    print_bell_numbers(Bell, 15)
    print(Bell[49][0])
    print('\n50th Bell number: ' + str(Bell[49][0]) + '\n')
    print('\nFirst 10 rows of Bell triangle:\n')
    print_bell_rows(Bell, 10)

main()