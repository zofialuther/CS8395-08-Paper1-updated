def divide(dividend, divisor):
    powersOf2 = []
    doublings = []
    line = 0
    while (2 ** line * divisor) <= dividend:
        powersOf2.append(2 ** line)
        doublings.append(2 ** line * divisor)
        line += 1
    answer = 0
    accumulator = 0
    for i in range(len(powersOf2)-1, -1, -1):
        if accumulator + doublings[i] <= dividend:
            accumulator += doublings[i]
            answer += powersOf2[i]
    print(answer, dividend - accumulator)

divide(580, 34)