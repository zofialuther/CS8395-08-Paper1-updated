from itertools import permutations

def main():
    for solution in queens(8):
        print(solution)

def queens(n):
    return [list(perm) for perm in permutations(range(1, n+1)) if is_solution(perm)]

def is_solution(perm):
    for i in range(len(perm)):
        for j in range(i+1, len(perm)):
            if abs(perm[i] - perm[j]) == abs(i - j):
                return False
    return True

if __name__ == "__main__":
    main()