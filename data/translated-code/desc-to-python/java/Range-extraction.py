class RangeExtraction:
    def __init__(self, numbers):
        self.numbers = numbers

    def get_ranges(self):
        ranges = []
        start = self.numbers[0]
        end = self.numbers[0]
        for i in range(1, len(self.numbers)):
            if self.numbers[i] == end + 1:
                end = self.numbers[i]
            else:
                if end - start >= 2:
                    ranges.append(f"{start}-{end}")
                else:
                    for j in range(start, end + 1):
                        ranges.append(str(j))
                start = self.numbers[i]
                end = self.numbers[i]
        if end - start >= 2:
            ranges.append(f"{start}-{end}")
        else:
            for j in range(start, end + 1):
                ranges.append(str(j))
        return ranges

if __name__ == "__main__":
    numbers = [1, 2, 3, 5, 6, 7, 9, 10, 11, 12, 15, 16, 20]
    range_extraction = RangeExtraction(numbers)
    result = range_extraction.get_ranges()
    for r in result:
        print(r)