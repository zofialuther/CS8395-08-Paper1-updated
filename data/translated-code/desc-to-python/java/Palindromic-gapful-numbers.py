def is_palindromic(num):
    return str(num) == str(num)[::-1]

def is_gapful(num):
    if len(str(num)) < 3:
        return False
    else:
        first_last_concat = int(str(num)[0] + str(num)[-1])
        return num % first_last_concat == 0

def getPalindromicGapfulEnding(ending, start=1):
    result = []
    num = start
    while len(result) < ending:
        if is_palindromic(num) and is_gapful(num):
            result.append(num)
        num += 1
    return result

def main():
    ending_20 = getPalindromicGapfulEnding(20)
    ending_15_100 = getPalindromicGapfulEnding(15, 100)
    ending_10_1000 = getPalindromicGapfulEnding(10, 1000)
    print("First 20 palindromic gapful numbers ending in 20:", ending_20)
    print("Last 15 of the first 100 palindromic gapful numbers:", ending_15_100)
    print("Last 10 of the first 1000 palindromic gapful numbers:", ending_10_1000)

main()