def for_loop(Hi, Lo, Step):
    if Step < 0 and Lo <= Hi:
        for i in range(Hi, Lo - 1, Step):
            print(i)

for_loop(10, 1, -1)