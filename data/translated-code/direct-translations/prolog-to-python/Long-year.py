def p(Year, P):
    P = (Year + (Year//4) - (Year//100) + (Year//400)) % 7

def long_year(Year):
    if p(Year, 4):
        return True
    else:
        Year_before = Year - 1
        return p(Year_before, 3)

def print_long_years(From, To):
    print("Long years between %w and %w:\n" % (From, To))
    print_long_years_helper(From, To, 0)
    print("\n")

def print_long_years_helper(From, To, Count):
    if From > To:
        return
    if long_year(From):
        if Count > 0:
            if Count % 10 == 0:
                print("\n")
            else:
                print(" ")
        print(From, end="")
        Count += 1
    Next = From + 1
    print_long_years_helper(Next, To, Count)

def main():
    print_long_years(1800, 2100)

main()