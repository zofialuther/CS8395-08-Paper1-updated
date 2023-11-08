class Harshad:
    
    def calculate_sum_of_digits(self, num):
        return sum(int(digit) for digit in str(num))
    
    def find_harshad_numbers(self, n):
        harshad_numbers = []
        num = 1
        while len(harshad_numbers) < n:
            if num % self.calculate_sum_of_digits(num) == 0:
                harshad_numbers.append(num)
            num += 1
        return harshad_numbers
    
    def find_next_harshad_number(self, start):
        num = start + 1
        while True:
            if num % self.calculate_sum_of_digits(num) == 0:
                return num
            num += 1

harshad = Harshad()
print(harshad.find_harshad_numbers(20))
print(harshad.find_next_harshad_number(1001))