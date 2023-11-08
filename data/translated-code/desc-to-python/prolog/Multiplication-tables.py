```python
def generate_table(S, E):
    try:
        print('   ', end='')
        for i in range(S, E + 1):
            print(f'{i:4}', end='')
        print()
        
        for i in range(S, E + 1):
            print(f'{i:2} |', end='')
            for j in range(S, E + 1):
                print(f'{i * j:4}', end='')
            print()
    except:
        pass
```