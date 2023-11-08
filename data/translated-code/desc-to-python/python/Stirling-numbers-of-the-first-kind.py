def sterling1(n, k, computed={}):
    if n == 0 and k == 0:
        return 1
    if n == 0 or k == 0:
        return 0
    if (n, k) in computed:
        return computed[(n, k)]
    
    computed[(n, k)] = sterling1(n-1, k-1, computed) + (n-1) * sterling1(n-1, k, computed)
    return computed[(n, k)]

max_val = 0
max_k = 0

for i in range(1, 13):
    val = sterling1(100, i)
    if val > max_val:
        max_val = val
        max_k = i
    print(f"S1(100, {i}): {val}")

print(f"The maximum value of S1(100, k) is {max_val} with {len(str(max_val))} digits at k={max_k}")