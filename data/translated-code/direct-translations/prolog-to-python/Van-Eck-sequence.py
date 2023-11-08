```python
def van_eck_init(_assoc):
    _assoc.clear()

def van_eck_next(Index, Last_term, Last_pos):
    if Last_term in Last_pos:
        V = Last_pos[Last_term]
        Next_term = Index - V
    else:
        Next_term = 0
    Index1 = Index + 1
    Last_pos1 = Last_pos.copy()
    Last_pos1[Last_term] = Index
    return (Index1, Next_term, Last_pos1)

def van_eck_sequence(N):
    V = (0, 0, {})
    return van_eck_sequence_helper(N, V)

def van_eck_sequence_helper(N, V):
    if N == 0:
        return []
    else:
        Index, Term, _ = V
        V1 = van_eck_next(Index, Term, V[2])
        Rest = van_eck_sequence_helper(N-1, V1)
        return [Term] + Rest

def write_list(From, To, List):
    for i in range(From-1, To):
        print(List[i], end=' ')
    print()

def main():
    Seq = van_eck_sequence(1000)
    print('First 10 terms of the Van Eck sequence:')
    write_list(1, 10, Seq)
    print('Terms 991 to 1000 of the Van Eck sequence:')
    write_list(991, 1000, Seq)

main()
```