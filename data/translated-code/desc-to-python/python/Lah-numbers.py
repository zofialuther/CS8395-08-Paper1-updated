import math

def lah_number(n, k):
    return math.comb(n-1, k-1) * math.factorial(n-k)

lah_table = {}
for n in range(13):
    lah_table[n] = [lah_number(n, k) for k in range(n+1)]

max_val = max(lah_table[100])
print(max_val)