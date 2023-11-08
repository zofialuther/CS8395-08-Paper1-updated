import re

class RangeExpander:
    def __init__(self, range):
        self.tokensIterator = iter(re.split(r'\s*,\s*', range))
        self.inRange = False
        self.upperRangeEndpoint = 0
        self.nextRangeValue = 0

    def hasNext(self):
        return self.hasNextRangeValue() or next(self.tokensIterator, None)

    def hasNextRangeValue(self):
        return self.inRange and self.nextRangeValue <= self.upperRangeEndpoint

    def __iter__(self):
        return self

    def __next__(self):
        if not self.hasNext():
            raise StopIteration

        if self.hasNextRangeValue():
            value = self.nextRangeValue
            self.nextRangeValue += 1
            return value

        token = next(self.tokensIterator)
        match = re.match(r'([+-]?\d+)-([+-]?\d+)', token)
        if match:
            self.inRange = True
            self.upperRangeEndpoint = int(match.group(2))
            self.nextRangeValue = int(match.group(1))
            return self.nextRangeValue
        else:
            self.inRange = False
            return int(token)

def main():
    re = RangeExpander("-6,-3--1,3-5,7-11,14,15,17-20")
    for i in re:
        print(i, end=" ")

if __name__ == "__main__":
    main()