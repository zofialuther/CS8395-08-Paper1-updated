```python
def init_palindrome(Digit, Next):
    Next = Digit * 10 - 1
    return Next

def next_palindrome(Digit, Power, Next, Even, Power1, Next2, Even1, Palindrome):
    Next1 = Next + 1
    if Next1 == Power * (Digit + 1):
        if Even == 1:
            Power1 = Power * 10
        else:
            Power1 = Power
        Next2 = Digit * Power1
        Even1 = 1 - Even
    else:
        Power1 = Power
        Next2 = Next1
        Even1 = Even

    if Even1 == 1:
        X = 10 * Power1
        Y = Next2
    else:
        X = Power1
        Y = Next2 // 10

    Z = reverse_number(Y)
    Palindrome = Next2 * X + Z
    return Palindrome

def reverse_number(N):
    return reverse_number_helper(N, 0)

def reverse_number_helper(N, Result):
    if N == 0:
        return Result
    else:
        R1 = Result * 10 + N % 10
        N1 = N // 10
        return reverse_number_helper(N1, R1)

def is_gapful(N):
    return is_gapful_helper(N, N)

def is_gapful_helper(N, M):
    if M < 10:
        return 0 == N % (N % 10 + 10 * (M % 10))
    else:
        M1 = M // 10
        return is_gapful_helper(N, M1)

def find_palindromic_gapful_numbers(N, List):
    return find_palindromic_gapful_numbers_helper(N, 1, List)

def find_palindromic_gapful_numbers_helper(N, Digit, List):
    if Digit == 10:
        return []
    else:
        Numbers = find_palindromic_gapful_numbers1(Digit, N)
        Next_digit = Digit + 1
        return [Numbers] + find_palindromic_gapful_numbers_helper(N, Next_digit, List)

def find_palindromic_gapful_numbers1(Digit, N):
    P = init_palindrome(Digit, 0)
    return find_palindromic_gapful_numbers1_helper(Digit, P, N, 0)

def find_palindromic_gapful_numbers1_helper(Digit, P, N, Count):
    if Count == N:
        return []
    else:
        P_next = next_palindrome(Digit, P, 0, 0, 0, 0, 0)
        Palindrome = P_next
        if is_gapful(Palindrome):
            Count1 = Count + 1
            Rest = find_palindromic_gapful_numbers1_helper(Digit, P_next, N, Count1)
            return [Palindrome] + Rest
        else:
            Count1 = Count
            Rest = find_palindromic_gapful_numbers1_helper(Digit, P_next, N, Count1)
            return Rest

def print_numbers(First, Last, Numbers):
    if First == 1:
        print("First", Last, "palindromic gapful numbers ending in:")
    else:
        Count = Last - First + 1
        print("Last", Count, "of first", Last, "palindromic gapful numbers ending in:")
    print_numbers_helper(First, Last, 1, Numbers)

def print_numbers_helper(First, Last, Digit, Numbers):
    if Digit == 10:
        return
    else:
        print(Digit, end=":")
        print_numbers1(First, Last, 1, Numbers)
        Next_digit = Digit + 1
        print_numbers_helper(First, Last, Next_digit, Numbers)

def print_numbers1(First, Last, I, Numbers):
    if I > Last:
        print()
    else:
        if I < First:
            I += 1
            print_numbers1(First, Last, I, Numbers)
        else:
            print(Numbers[I-1], end=" ")
            I += 1
            print_numbers1(First, Last, I, Numbers)

def main():
    Numbers = find_palindromic_gapful_numbers(1000, [])
    print_numbers(1, 20, Numbers)
    print_numbers(86, 100, Numbers)
    print_numbers(991, 1000, Numbers)

main()
```