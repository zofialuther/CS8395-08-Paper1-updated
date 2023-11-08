MAX = 250
p5, sum2 = {}, {}

for i in range(1, MAX):
    p5[i**5] = i
    for j in range(i, MAX):
        sum2[i**5 + j**5] = (i, j)

sk = sorted(sum2.keys())
for p in sorted(p5.keys()):
    for s in sk:
        if p <= s:
            break
        if p - s in sum2:
            print(p5[p], sum2[s][0], sum2[s][1], sum2[p-s][0], sum2[p-s][1])
            exit()
            
This code appears to perform some sort of computation and prints some values based on conditions.