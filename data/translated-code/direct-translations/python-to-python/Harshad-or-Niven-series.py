import itertools

def harshad():
    for n in itertools.count(1):
        if n % sum(int(ch) for ch in str(n)) == 0:
            yield n

harshad_list = list(itertools.islice(harshad(), 0, 20))
print(harshad_list)

for n in harshad():
    if n > 1000:
        print(n)
        break