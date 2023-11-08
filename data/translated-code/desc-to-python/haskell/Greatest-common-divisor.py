def gcd(a, b):
    a = abs(a)
    b = abs(b)
    
    def gcd_(a, b):
        if b == 0:
            return a
        else:
            return gcd_(b, a % b)
    
    return gcd_(a, b)