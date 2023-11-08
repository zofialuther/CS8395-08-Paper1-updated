def accumulator(sum0):
    sum = [sum0]

    def inner_function(n):
        if longable(sum[0]) and longable(n):
            sum[0] = sum[0] + n
        else:
            sum[0] = sum[0] + n
        return sum[0]

    return inner_function

def longable(n):
    return isinstance(n, (int, float))

x = accumulator(1)
x(5)
accumulator(3)
print(x(2.3))