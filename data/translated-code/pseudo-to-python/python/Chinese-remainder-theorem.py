def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    
    for i in range(len(n)):
        p = prod / n[i]
        sum = sum + a[i] * mul_inv(p, n[i]) * p
    
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0 = 0
    x1 = 1
    
    if b == 1:
        return 1
    
    while a > 1:
        q = a / b
        temp = a
        a = b
        b = temp % b
        temp = x0
        x0 = x1 - q * x0
        x1 = temp
    
    if x1 < 0:
        x1 = x1 + b0
    
    return x1

if __name__ == '__main__':
    n = [3, 5, 7]
    a = [2, 3, 2]
    print(chinese_remainder(n, a))