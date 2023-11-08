```python
# Size of the 2D grid
grid_size = 300
# Number of generations
generations = 1000

# Main procedure: generate n generations of life and store each file.
def cellular(I):
    M = read_pbm(I + '0.0000.pbm', grid_size)
    cellular_(I, M, grid_size, 1)

def cellular_(I, M, GS, N):
    N1 = N + 1
    N0 = '{:04d}'.format(N)
    I1 = I + N0 + '.pbm'
    step(M, M1)
    write_pbm(M1, GS, I1)
    if N1 < generations:
        cellular_(I, M1, GS, N1)

def step([R1, R2, *M], [H, *T]):
    step_ss(R1, R2, H)
    step_([R1, R2, *M], T)

def step_([R1, R2, R3, *M], [H, *T]):
    step_ii(R1, R2, R3, H)
    step_([R2, R3, *M], T)

def step_([R1, R2], [H]):
    step_ee(R1, R2, H)

# ... (continue translating the rest of the pseudocode)
```