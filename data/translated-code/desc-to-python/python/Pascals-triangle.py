def pascal(n):
    row = []
    k = [1]
    for i in range(n):
        row = [1]
        for j in range(1, i):
            row.append(k[j-1] + k[j])
        if(i != 0):
            row.append(1)
        print(row)
        k = row
    return True