def isHappy(num):
    def p(n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = f(n)
        return n == 1
    
    def f(n):
        sum = 0
        while n:
            n, digit = divmod(n, 10)
            sum += digit ** 2
        return sum
    
    happy_nums = []
    i = 1
    while len(happy_nums) < 8:
        if p(i):
            happy_nums.append(i)
        i += 1
    print(happy_nums)