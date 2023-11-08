class RN:
    class Numeral:
        def __init__(self, weight):
            self.weight = weight

    def roman(n):
        if n <= 0:
            raise ValueError()
        
        buf = []
        values = [
            Numeral(1), Numeral(4), Numeral(5), Numeral(9), Numeral(10),
            Numeral(40), Numeral(50), Numeral(90), Numeral(100), Numeral(400),
            Numeral(500), Numeral(900), Numeral(1000)
        ]
        
        for i in range(len(values) - 1, -1, -1):
            while n >= values[i].weight:
                buf.append(values[i])
                n -= values[i].weight
        
        return ''.join(str(x) for x in buf)

    def test(n):
        print(str(n) + " = " + roman(n))

    if __name__ == "__main__":
        test(1999)
        test(25)
        test(944)
        test(0)