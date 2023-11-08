```python
# Size of the 2D grid
grid_size = 300
# Number of generations
generations = 1000

# Main procedure: generate n generations of life and store each file.
def cellular(I):
    GS = grid_size
    I1 = I + '0.0000.pbm'
    M = read_pbm(I1, GS)
    cellular_(I, M, GS, 1)

def cellular_(I, M, GS, N):
    N1 = N + 1
    N0 = str(N).zfill(4)
    I1 = I + N0 + '.pbm'
    M1 = step(M)
    write_pbm(M1, GS, I1)
    cellular_(I, M1, GS, N1)

# Apply the Game Of Life rule set to every cell.
def step(M):
    result = []
    for i in range(len(M)):
        if i == 0:
            result.append(step_ss(M[i]))
        elif i == len(M) - 1:
            result.append(step_ee(M[i-1], M[i]))
        else:
            result.append(step_ii(M[i-1], M[i], M[i+1]))
    return result

def step_ss(R):
    result = []
    for i in range(len(R)):
        if i == 0:
            result.append(rule([0, 0, 0], [0, R[i], R[i+1]], [0, R[i], R[i+1]]))
        elif i == len(R) - 1:
            result.append(rule([0, R[i-1], R[i]], [0, R[i-1], R[i]], [0, 0, 0]))
        else:
            result.append(rule([0, R[i-1], R[i]], [0, R[i-1], R[i]], [0, R[i+1], R[i+2]]))
    return result

# Remaining rule functions to be defined similarly

# Read a 2bit Protable Bitmap into a GS x GS 2-dimensional list
def read_pbm(F, GS):
    with open(F, 'r') as file:
        # Read and process the file to create the 2D list
        pass

# Write a GS x GS 2-dimensional list into a 2bit Protable Bitmap
def write_pbm(L, GS, F):
    with open(F, 'w') as file:
        file.write('P1\n')
        file.write(f'{GS} {GS}\n')
        # Write the 2D list to the file
```