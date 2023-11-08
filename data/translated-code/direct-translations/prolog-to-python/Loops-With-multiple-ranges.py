```python
def plus(a, b, c):
    return a + b == c

def for_loop(Lo, Hi, Step, Lo):
    if Step > 0 and Lo <= Hi:
        return True
    else:
        return False

def translate(V):
    if isinstance(V, (int, float)):
        return V
    elif V in sym_dict:
        return sym_dict[V]
    elif isinstance(V, str):
        if V[0] == "-":
            return -1 * translate(V[1:])
        elif "+" in V:
            a, b = V.split("+")
            return translate(a) + translate(b)
        elif "-" in V:
            a, b = V.split("-")
            return translate(a) - translate(b)
        elif "^" in V:
            a, b = V.split("^")
            return translate(a) ** translate(b)

def for_loop(Lo, Hi, Step, Val):
    if Step > 0 and plus(Lo, Step, V) and V <= Hi:
        return for_loop(V, Hi, Step, Val)
    elif Step < 0 and plus(Hi, Step, V) and Lo <= V:
        return for_loop(V, Lo, Step, Val)

sym_dict = {
    "x": 5,
    "y": -5,
    "z": -2,
    "one": 1,
    "three": 3,
    "seven": 7
}

def range_value(Val):
    for Lo, Hi, Step in ranges:
        F = translate(Lo)
        T = translate(Hi)
        S = translate(Step)
        for_loop(F, T, S, Val)

def calc_values(Values):
    S = 0
    P = 1
    for J in Values:
        S0 = S + abs(J)
        if abs(P) < 2**27 and J != 0:
            P0 = P * J
        else:
            P0 = P
        S = S0
        P = P0
    return S, P

ranges = [
    ("-three", "3^3", "three"),
    ("-seven", "seven", "x"),
    ("555", "550-y", "1"),
    ("22", "-28", "-three"),
    ("1927", "1939", "1"),
    ("x", "y", "z"),
    ("11^x", "11^x+one", "1")
]

Values = []
for range in ranges:
    range_value(range)
    S, P = calc_values(Values)
    print(S, P)
```