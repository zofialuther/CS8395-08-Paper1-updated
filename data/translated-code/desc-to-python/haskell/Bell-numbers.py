def bellTri(n):
    bell = [[0 for i in range(n)] for j in range(n)]
    bell[0][0] = 1
    for i in range(1, n):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell

def bell(n):
    triangle = bellTri(n)
    bell_numbers = [row[0] for row in triangle]
    return bell_numbers

def main():
    triangle = bellTri(10)
    for row in triangle:
        print(row)
    
    bell_nums = bell(15)
    print(bell_nums)
    
    print(bell(50))

main()