```python
def b_not(input, out):
    if input == "hi":
        out = "lo"
    else:
        out = "hi"

def b_and(in1, in2, out):
    if in1 == "hi" and in2 == "hi":
        out = "hi"
    else:
        out = "lo"

def b_or(in1, in2, out):
    if in1 == "hi" or in2 == "hi":
        out = "hi"
    else:
        out = "lo"

def b_xor(input, out):
    b_not(input, "NotA")
    b_not(input, "NotB")
    b_and(input, "NotB", "P")
    b_and("NotA", input, "Q")
    b_or("P", "Q", out)

def b_half_adder(input, s, c):
    b_xor(input, "S")
    b_and(input, "S", "C")

def b_full_adder(input, s, c):
    b_half_adder(input, "S0", "C0")
    b_half_adder("S0", s, "C")
    b_or("C0", "C", "C1")

def b_4_bit_adder(A, B, S, V):
    b_full_adder("A0", "B0", "lo", "S0", "C0")
    b_full_adder("A1", "B1", "C0", "S1", "C1")
    b_full_adder("A2", "B2", "C1", "S2", "C2")
    b_full_adder("A3", "B3", "C2", "S3", V)

def test_add(A, B, T):
    b_4_bit_adder(A, B, "R", "C")
    print(f'{A} + {B} is {R} {C} \t({T})')

def go():
    test_add("hi", "lo", "lo", "lo", "hi", "lo", "lo", "lo", "1 + 1 = 2")
    test_add("lo", "hi", "lo", "lo", "lo", "hi", "lo", "lo", "2 + 2 = 4")
    test_add("hi", "lo", "hi", "lo", "hi", "lo", "lo", "hi", "5 + 9 = 14")
    test_add("hi", "hi", "lo", "hi", "hi", "lo", "lo", "hi", "11 + 9 = 20")
    test_add("lo", "lo", "lo", "hi", "lo", "lo", "lo", "hi", "8 + 8 = 16")
    test_add("hi", "hi", "hi", "hi", "hi", "lo", "lo", "lo", "15 + 1 = 16")
```