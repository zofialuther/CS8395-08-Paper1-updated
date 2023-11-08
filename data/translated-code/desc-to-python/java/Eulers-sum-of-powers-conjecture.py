```python
# Python code
# Solve the Euler sum of powers conjecture

# Pre-calculate fifth powers
fifth_powers = [i**5 for i in range(251)]

# Iterate through all possible combinations of five numbers
for a in range(251):
    for b in range(251):
        for c in range(251):
            for d in range(251):
                for e in range(251):
                    if fifth_powers[a] + fifth_powers[b] + fifth_powers[c] + fifth_powers[d] + fifth_powers[e] in fifth_powers:
                        print(f"{a}^5 + {b}^5 + {c}^5 + {d}^5 + {e}^5 = {fifth_powers[a] + fifth_powers[b] + fifth_powers[c] + fifth_powers[d] + fifth_powers[e]}")
```