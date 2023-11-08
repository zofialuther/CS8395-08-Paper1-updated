```python
def pi_spigot():
    pi(3, 3, 40).

pi(A, B, N) :-
    N > 0,
    C is A * 10,
    D is C div B,
    E is C mod B,
    F is B * 10,
    pi(D, E, N-1),
    (N = 1, write(D); true).
```