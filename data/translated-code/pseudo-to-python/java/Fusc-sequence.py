fusc = [0, 1]

for n in range(2, 61):
    fusc.append(fusc[n-1] + fusc[n-2])

for n in range(61):
    print(fusc[n], end=" ")

max_length = 0
max_index = 0
for i in range(6):
    if i != 0:
        val = 10**i
    else:
        val = -1
    for j in range(max_index, len(fusc)):
        if len(str(fusc[j])) > max_length:
            max_length = len(str(fusc[j]))
            max_index = j
            print("fusc[", j, "] = ", fusc[j])
            break