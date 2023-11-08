def Zig_Zag(size):
    data = [[0 for _ in range(size)] for _ in range(size)]
    i = 1
    j = 1
    for element in range(size * size):
        data[i - 1][j - 1] = element
        if (i + j) % 2 == 0:
            # Even stripes
            if j < size:
                j += 1
            else:
                i += 2
            if i > 1:
                i -= 1
        else:
            # Odd stripes
            if i < size:
                i += 1
            else:
                j += 2
            if j > 1:
                j -= 1
    return data