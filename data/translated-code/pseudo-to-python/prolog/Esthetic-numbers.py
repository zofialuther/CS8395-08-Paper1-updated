```python
def main():
    for Base in range(2, 16):
        Min_index = Base * 4
        Max_index = Base * 6
        print_esthetic_numbers1(Base, Min_index, Max_index)
    
    print_esthetic_numbers2(1000, 9999, 16)
    print_new_line()
    print_esthetic_numbers2(100000000, 130000000, 8)

def print_esthetic_numbers1(Base, Min_index, Max_index):
    Format = str(Base)
    print("Esthetic numbers in base " + str(Base) + " from index " + str(Min_index) + " through index " + str(Max_index) + ":")
    print_esthetic_numbers1_helper(Base, Format, Min_index, Max_index, 0, 1)

def print_esthetic_numbers1_helper(Base, Format, Min_index, Max_index, M, I):
    while I <= Max_index:
        N = next_esthetic_number(Base, M)
        if I >= Min_index:
            Format += " " + str(N)
        I = I + 1
        print_esthetic_numbers1_helper(Base, Format, Min_index, Max_index, N, I)

def print_esthetic_numbers2(Min, Max, Per_line):
    print("Esthetic numbers in base 10 between " + str(Min) + " and " + str(Max) + ":")
    M = Min - 1
    count = 0
    print_esthetic_numbers2_helper(Max, Per_line, M, count)

def print_esthetic_numbers2_helper(Max, Per_line, M, Count):
    N = M
    while N <= Max:
        N = next_esthetic_number(10, M)
        print(N, end=" ")
        Count = Count + 1
        if Count % Per_line == 0:
            print()
        print_esthetic_numbers2_helper(Max, Per_line, N, Count)

def next_esthetic_number(Base, M):
    N = M + 1
    if N < Base:
        return N
    else:
        A = M // Base
        B = A % Base
        if B == M % Base + 1 and B + 1 < Base:
            return M + 2
        else:
            C = next_esthetic_number(Base, A)
            D = C % Base
            if D == 0:
                E = 1
            else:
                E = D - 1
            return C * Base + E
```