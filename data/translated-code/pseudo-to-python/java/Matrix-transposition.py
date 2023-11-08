def transposeMatrix(m):
    ans = [[0 for i in range(len(m))] for j in range(len(m[0]))]
    for rows in range(len(m)):
        for cols in range(len(m[0])):
            ans[cols][rows] = m[rows][cols]
    for i in ans:
        print(i)