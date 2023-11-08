class RangeConsolidation:
    def main(self, ranges):
        self.displayRanges(ranges)

    @staticmethod
    def displayRanges(ranges):
        sorted_ranges = sorted(ranges, key=RangeSorter())
        consolidated_ranges = []
        for r in sorted_ranges:
            consolidated = False
            for cr in consolidated_ranges:
                if r.consolidate(cr):
                    consolidated = True
                    break
            if not consolidated:
                consolidated_ranges.append(r)
        consolidated_ranges.sort(key=RangeSorter())
        return consolidated_ranges


class RangeSorter:
    def __init__(self):
        pass

    def __call__(self, r):
        return r.left


class Range:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def consolidate(self, other):
        if self.left <= other.right and self.right >= other.left:
            self.left = min(self.left, other.left)
            self.right = max(self.right, other.right)
            return True
        return False

    def __str__(self):
        return f'({self.left}, {self.right})'

    @staticmethod
    def consolidate(ranges):
        sorted_ranges = sorted(ranges, key=RangeSorter())
        consolidated_ranges = []
        for r in sorted_ranges:
            consolidated = False
            for cr in consolidated_ranges:
                if r.consolidate(cr):
                    consolidated = True
                    break
            if not consolidated:
                consolidated_ranges.append(r)
        consolidated_ranges.sort(key=RangeSorter())
        return consolidated_ranges
