class LexicographicalNumbers:
    def lexOrder(self, n):
        return sorted(range(1, n+1), key=str)

    def main(self):
        example_inputs = [5, 10, 15, 20]
        for i in example_inputs:
            print(self.lexOrder(i))