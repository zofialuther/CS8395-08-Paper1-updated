Base = 16
N = 4
Paddy_cnt = 1
for V in range(1, Base**N):
    for B in range(1, N*2-1):
        x = V * V // (Base**B)
        y = V * V % (Base**B)
        if V == x + y and y > 0:
            print(hex(V), Paddy_cnt)
            Paddy_cnt += 1
            break