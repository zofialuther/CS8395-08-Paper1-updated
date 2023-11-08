import random

print("number reversal game")
data = list('123456789')
trials = 0

while data == sorted(data):
    random.shuffle(data)

while data != sorted(data):
    trials = trials + 1
    print("#%2i: LIST: %r" % (trials, ' '.join(data)))
    flip = int(input("Flip how many?: "))
    data[:flip] = list(reversed(data[:flip]))

print("You took %2i attempts to put the digits in order!" % trials)