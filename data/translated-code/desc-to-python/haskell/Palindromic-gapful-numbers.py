```python
def is_gapful(num):
    return num % int(str(num)[0] + str(num)[-1]) == 0

def generate_palindromic_num():
    palindromic_nums = []
    for num in range(10, 100):
        if str(num) == str(num)[::-1]:
            palindromic_nums.append(num)
    return palindromic_nums

def filter_ending_digit(nums, digit):
    filtered_nums = [num for num in nums if str(num)[-1] == str(digit)]
    return filtered_nums

def display_numbers(nums):
    print(nums)

def main():
    palindromic_nums = generate_palindromic_num()
    
    palindromic_gapful_20 = filter_ending_digit([num for num in palindromic_nums if is_gapful(num)], 0)[:20]
    display_numbers(palindromic_gapful_20)
    
    palindromic_gapful_15_last_100 = filter_ending_digit([num for num in palindromic_nums if is_gapful(num)], 0)[-15:]
    display_numbers(palindromic_gapful_15_last_100)
    
    palindromic_gapful_10_last_1000 = filter_ending_digit([num for num in palindromic_nums if is_gapful(num)], 0)[-10:]
    display_numbers(palindromic_gapful_10_last_1000)

if __name__ == "__main__":
    main()
```