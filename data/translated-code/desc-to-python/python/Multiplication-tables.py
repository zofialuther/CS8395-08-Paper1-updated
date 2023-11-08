```python
def generate_table(dim):
    return [(i, j, i*j) for i in range(1, dim+1) for j in range(i, dim+1)]

def bind(lst, func):
    return [elem for x in lst for elem in func(x)]

def main():
    dim = 5
    table1 = generate_table(dim)
    table2 = bind(list(range(1, dim+1)), lambda x: bind(list(range(x, dim+1)), lambda y: [(x, y, x*y)]))
    print(table1)
    print(table2)

main()
```