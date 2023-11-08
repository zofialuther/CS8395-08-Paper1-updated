```python
Base = 16
N = 4
Paddy_cnt = 1
for V in range(1, Base**N + 1):
    for B in range(1, N*2-1):
        x, y = divmod(V*V, Base**B)
        if V == x+y and 0 < y:
            print('{1}: {0:x}'.format(V, Paddy_cnt))
            Paddy_cnt += 1
            break
```