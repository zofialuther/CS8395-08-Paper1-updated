def int2bin(num):
    binary_list = []
    while num > 0:
        binary_list.insert(0, num % 2)
        num = num // 2
    return binary_list

def bin2int(binary_list):
    decimal = 0
    for i in range(len(binary_list)):
        decimal += binary_list[i] * (2 ** (len(binary_list) - 1 - i))
    return decimal