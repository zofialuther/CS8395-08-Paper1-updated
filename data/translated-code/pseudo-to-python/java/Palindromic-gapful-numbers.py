map_palindromic_gapful = {}
map_count = {}

for i in range(1, 10):
    map_palindromic_gapful[i] = []
    map_count[i] = 0

not_populated = True
n = 101
while not_populated:
    if is_gapful(n):
        index = int(str(n)[-1])
        if map_count[index] < first_how_many:
            map_palindromic_gapful[index].append(n)
            map_count[index] += 1
            if len(map_palindromic_gapful[index]) > count_returned:
                map_palindromic_gapful[index].pop(0)
        finished = True
        for i in range(1, 10):
            if map_count[i] < first_how_many:
                finished = False
                break
        if finished:
            not_populated = False
    n = next_palindrome(n)

return map_palindromic_gapful