def dotProd(a, b):
    if len(a) != len(b):
        raise ValueError("The dimensions have to be equal!")
    
    sum = 0
    for i in range(len(a)):
        sum = sum + (a[i] * b[i])
    
    return sum

def main():
    a = [1, 3, -5]
    b = [4, -2, -1]
    
    print(dotProd(a, b))

main()