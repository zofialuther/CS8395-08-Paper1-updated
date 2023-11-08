class SumMultiples:
    def calculate_sum(self, limit):
        sum = 0
        for i in range(limit):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum

if __name__ == "__main__":
    obj = SumMultiples()
    result = obj.calculate_sum(1000)
    print(result)