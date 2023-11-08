def accumulator(starting_value):
    total = starting_value
    while True:
        value = yield total
        total += value

acc1 = accumulator(1)
print(acc1.send(5))

acc2 = accumulator(3)
print(acc2.send(2.3)