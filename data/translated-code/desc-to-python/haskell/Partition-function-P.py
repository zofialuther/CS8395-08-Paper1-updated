class Memo:
    def __init__(self):
        self.memo = {}

def memo(memo_obj, num):
    if num in memo_obj.memo:
        return memo_obj.memo[num]
    if num <= 1:
        result = 1
    else:
        result = num * memo(memo_obj, num - 1)
    memo_obj.memo[num] = result
    return result

def calculate_partition(num):
    memo_obj = Memo()
    return memo(memo_obj, num)

def main():
    print(calculate_partition(6666))

main()