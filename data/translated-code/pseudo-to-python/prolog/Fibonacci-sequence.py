X = 15
A = [0, 1]

for i in range(2, X):
    next_num = A[i-1] + A[i-2]
    A.append(next_num)

print(A)