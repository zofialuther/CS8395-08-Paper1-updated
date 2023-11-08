class SumMultiples:
    def getSum(n):
        sum = 0
        for i in range(3, n):
            if i % 3 == 0 or i % 5 == 0:
                sum += i
        return sum
    
    def main(args):
        print(SumMultiples.getSum(1000))