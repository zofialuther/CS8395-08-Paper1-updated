```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("library(clpfd)")

def compound_time(N):
    times(N, R)
    print(f"{N}: ", end="")
    write_times(R)

def write_times(T):
    if T:
        Tt, Val = T[0]
        if len(T) > 1:
            print(f"{Val} {Tt}, ", end="")
            write_times(T[1:])
        else:
            print(f"{Val} {Tt}")

def times(N, R):
    TTs = [T for T, _ in prolog.query("time_type(T, _)")]
    times(TTs, N, R)

def time_type(Tt, Div):
    prolog.assertz(f"time_type({Tt}, {Div})")

def times(T, N, Rest):
    if not T:
        Rest = []
    else:
        Tt, Div = prolog.query("time_type(Tt, Div)").next()
        Val = N // Div
        if Val < 1:
            times(T[1:], N, Rest)
        else:
            Rem = N % Div
            times(T[1:], Rem, Rest)
            Rest.insert(0, [Tt, Val])

time_type("wk", 60 * 60 * 24 * 7)
time_type("d", 60 * 60 * 24)
time_type("hr", 60 * 60)
time_type("min", 60)
time_type("sec", 1)
```