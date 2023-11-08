class Proper:
    def properDivs(self, num):
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors

if __name__ == "__main__":
    p = Proper()
    for i in range(1, 11):
        print(f"Proper divisors of {i}: {p.properDivs(i)}")
    
    max_divisors = 0
    max_num = 0
    for i in range(1, 20001):
        div_count = len(p.properDivs(i))
        if div_count > max_divisors:
            max_divisors = div_count
            max_num = i
    print(f"The number between 1 and 20000 with the most proper divisors is {max_num} with {max_divisors} proper divisors.")