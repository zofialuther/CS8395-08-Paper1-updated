def div(a, b):
    if b == 0:
        return 999999.0
    else:
        return a / b

ops = {'mul': '*', 'div': '/', 'sub': '-', 'add': '+'}

def solve24(num, how, target):
    if len(num) == 1:
        if round(num[0], 5) == round(target, 5):
            return str(how[0]).replace(',', '').replace("'", '')
    else:
        for i in range(len(num)):
            for j in range(len(num)):
                if i != j:
                    for op in ops:
                        new_num = [n for k, n in enumerate(num) if k != i and k != j] + [div(num[i], num[j])]
                        new_how = [h for k, h in enumerate(how) if k != i and k != j] + [(how[i], ops[op], how[j])]
                        yield from solve24(new_num, new_how, target)

tests = [
         [1, 7, 2, 7],
         [5, 7, 5, 4],
         [1, 4, 6, 6],
         [2, 3, 7, 3],
         [1, 6, 2, 6],
         [7, 9, 4, 1],
         [6, 4, 2, 2],
         [5, 7, 9, 7],
         [3, 3, 8, 8],
         [8, 7, 9, 7],
         [9, 4, 4, 5]
        ]

for nums in tests:
    print(nums, " : ")
    try:
        print(next(solve24(nums, nums, 24)))
    except StopIteration:
        print("No solution found")