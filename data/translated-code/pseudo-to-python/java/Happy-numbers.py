class Happy:
    @staticmethod
    def happy(number):
        m = 0
        digit = 0
        cycle = set()
        while number != 1 and number not in cycle:
            m = 0
            while number > 0:
                digit = int(number % 10)
                m += digit*digit
                number //= 10
            number = m
            cycle.add(number)
        return number == 1

    @staticmethod
    def main():
        num = 1
        count = 0
        while count < 8:
            if Happy.happy(num):
                print(num)
                count += 1
            num += 1