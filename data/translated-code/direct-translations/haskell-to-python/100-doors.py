n = 10

def toggleEvery(k):
    return [1 if i % (k+1) == 0 else 0 for i in range(n+1)]

result = [i for i in range(n+1) if i % 2 != 0]
print(result)