```python
import math

# Fibonacci sequence generator
def fib(C, P, S, Cv, V):
    if C == 0:
        N = P + S
    else:
        Cn = C + 1
        N = P + S
        fib(Cn, S, N, Cv, V)

def fibonacci(C):
    if C == 0:
        return 0
    elif C == 1:
        return 1
    else:
        return fib(2, 0, 1, C, 0)

# The Benford law calculated
def benford(D):
    return math.log10(1 + 1/D)

# Retrieves the first characters of the first 1000 fibonacci numbers (excluding zero)
def firstchar():
    result = []
    for i in range(1, 1000):
        n = fibonacci(i)
        if n != 0:
            first_char = str(n)[0]
            result.append(int(first_char))
    return result

# Increment the n'th list item (1 based), result -> third argument
def incNth(H, lst):
    lst[H-1] += 1

# Calculate the frequency of all the list items
def freq(lst):
    length = len(lst)
    minimum = min(lst)
    maximum = max(lst)
    freq_list = [0] * (maximum - minimum + 1)
    for num in lst:
        freq_list[num - minimum] += 1
    return [val/length for val in freq_list]

# Output the results
def writeHdr():
    print('{:<15} - {:<15}'.format('Benford', 'Measured'))

def writeData(Benford, Freq):
    print('{:<15.2f}% - {:<15.2f}%'.format(Benford*100, Freq*100))

def go():
    Benford = [benford(N) for N in range(1, 10)]
    Fc = firstchar()
    Freq = freq(Fc)
    writeHdr()
    for b, f in zip(Benford, Freq):
        writeData(b, f)

# main goal
go()
```