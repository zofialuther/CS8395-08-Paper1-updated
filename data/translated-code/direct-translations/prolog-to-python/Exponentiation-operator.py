```python
def exp_folder(Base, Power, Powers):
    Power = Base * Powers
    return Power

def power_function(Base, Exp, Power):
    if Exp < 0:
        Power = 1 / (Base ** (Exp * -1))
    elif Exp > 0:
        Powers = [None] * Exp
        Power = 1
        for i in range(Exp):
            Power = exp_folder(Base, Power, Powers[i])
    else:
        Power = 1
    return Power
```