from constraint import *

problem = Problem()

problem.addVariable('N', [1, 2, 3, 4, 5])
problem.addVariable('R1', [1, 2, 3, 4, 5])
problem.addVariable('R2', [1, 2, 3, 4, 5])
problem.addVariable('N1', [1, 2, 3, 4, 5])
problem.addVariable('S1', [1, 2, 3, 4, 5])
problem.addVariable('R', [1, 2, 3, 4, 5])
problem.addVariable('S', [1, 2, 3, 4, 5])
problem.addVariable('V', [1, 2, 3, 4, 5])
problem.addVariable('N2', [1, 2, 3, 4, 5])

def ffr(N, R1, R2):
    return R1 == R2

def ffs(N, R1, R2):
    return R1 == R2

def hofstadter(N):
    return True

problem.addConstraint(ffr, ['N', 'R1', 'R2'])
problem.addConstraint(ffs, ['N', 'R1', 'R2'])

def rule1(N, R, R1, N1, S1):
    if N > 1:
        N1 = N - 1
        R = R1 + S1

problem.addConstraint(rule1, ['N', 'R', 'R1', 'N1', 'S1'])

def rule2(N, S, N1, S1):
    if N > 1:
        N1 = N - 1
        V = S1 + 1
        if find_chr_constraint((_, V)):
            S = V + 1
        else:
            S = V

problem.addConstraint(rule2, ['N', 'S', 'N1', 'S1'])

def rule3(N):
    return ffr(1, 1) and ffs(1, 2)

problem.addConstraint(rule3, ['N'])

def rule4(N, N1, R, S):
    if N1 < N:
        N2 = N1 + 1
        ffr(N2, _) and ffs(N2, _)

problem.addConstraint(rule4, ['N', 'N1', 'R', 'S'])