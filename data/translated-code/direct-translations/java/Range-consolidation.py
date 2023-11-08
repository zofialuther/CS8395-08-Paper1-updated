```python
class Range:
    def __init__(self, left, right):
        if left <= right:
            self.left = left
            self.right = right
        else:
            self.left = right
            self.right = left

    def consolidate(self, other):
        if self.right < other.left:
            return None
        if other.right < self.left:
            return None
        if self.left <= other.left and self.right >= other.right:
            return self
        if other.left <= self.left and other.right >= self.right:
            return other
        if self.left <= other.left and self.right <= other.right:
            return Range(self.left, other.right)
        if self.left >= other.left and self.right >= other.right:
            return Range(other.left, self.right)
        raise RuntimeError("ERROR: Logic invalid.")

    def __str__(self):
        return "[" + str(self.left) + ", " + str(self.right) + "]"

    @staticmethod
    def consolidate(ranges):
        consolidated = []

        ranges.sort(key=lambda x: x.left)

        for inRange in ranges:
            r = None
            conRange = None
            for conRangeLoop in consolidated:
                r = inRange.consolidate(conRangeLoop)
                if r is not None:
                    conRange = conRangeLoop
                    break
            if r is None:
                consolidated.append(inRange)
            else:
                consolidated.remove(conRange)
                consolidated.append(r)

        consolidated.sort(key=lambda x: x.left)

        return consolidated


def display_ranges(ranges):
    print("ranges = %-70s, consolidated = %s" % (ranges, Range.consolidate(ranges)))


def main():
    display_ranges([Range(1.1, 2.2)])
    display_ranges([Range(6.1, 7.2), Range(7.2, 8.3)])
    display_ranges([Range(4, 3), Range(2, 1)])
    display_ranges([Range(4, 3), Range(2, 1), Range(-1, -2), Range(3.9, 10)])
    display_ranges([Range(1, 3), Range(-6, -1), Range(-4, -5), Range(8, 2), Range(-6, -6)])
    display_ranges([Range(1, 1), Range(1, 1)])
    display_ranges([Range(1, 1), Range(1, 2)])
    display_ranges([Range(1, 2), Range(3, 4), Range(1.5, 3.5), Range(1.2, 2.5)])


if __name__ == "__main__":
    main()
```