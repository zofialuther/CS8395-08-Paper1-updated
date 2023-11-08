def pascal(n):
    pascalTriangle = []
    for i in range(n):
        row = [0]*(i+1)
        for j in range(i+1):
            if j == 0 or j == i:
                row[j] = 1
            else:
                row[j] = pascalTriangle[i-1][j-1] + pascalTriangle[i-1][j]
        print(row)
        pascalTriangle.append(row)