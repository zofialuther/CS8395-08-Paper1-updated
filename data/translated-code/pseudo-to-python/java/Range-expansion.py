class RangeExpander:
    TOKEN_PATTERN = "([+-]?\d+)-([+-]?\d+)"

    def __init__(self, range):
        self.tokensIterator = iter(list(range.split(",")))
        self.inRange = False
        self.upperRangeEndpoint = 0
        self.nextRangeValue = 0

    def hasNext(self):
        return self.hasNextRangeValue() or next(self.tokensIterator, None) is not None

    def hasNextRangeValue(self):
        return self.inRange and self.nextRangeValue <= self.upperRangeEndpoint

    def next(self):
        if not self.hasNext():
            raise NoSuchElementException
        if self.hasNextRangeValue():
            result = self.nextRangeValue
            self.nextRangeValue += 1
            return result
        token = next(self.tokensIterator)
        match = re.match(TOKEN_PATTERN, token)
        if match:
            self.inRange = True
            self.upperRangeEndpoint = int(match.group(2))
            self.nextRangeValue = int(match.group(1))
            self.nextRangeValue += 1
            return self.nextRangeValue
        self.inRange = False
        return int(token)

    def __iter__(self):
        return self

class RangeExpanderTest:
    def main(self, args):
        re = RangeExpander("-6,-3--1,3-5,7-11,14,15,17-20")
        for value in re:
            print(value)