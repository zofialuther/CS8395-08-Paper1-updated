def repString(n, s):
    result = ""
    binary_n = bin(n)[2:]
    duplicated_s = (x for _ in range(n) for x in s)
    for d, x in zip(binary_n, duplicated_s):
        if int(d) > 0:
            result = result + x
    return result

print(repString(500, "ha"))