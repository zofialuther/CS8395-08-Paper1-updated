class SpellingOfOrdinalNumbers:

    @staticmethod
    def main(args):
        for test in [1, 2, 3, 4, 5, 11, 65, 100, 101, 272, 23456, 8007006005004003]:
            print(f"{test} = {SpellingOfOrdinalNumbers.toOrdinal(test)}")

    ordinalMap = {
        "one": "first",
        "two": "second",
        "three": "third",
        "five": "fifth",
        "eight": "eighth",
        "nine": "ninth",
        "twelve": "twelfth"
    }

    @staticmethod
    def toOrdinal(n):
        spelling = SpellingOfOrdinalNumbers.numToString(n)
        split = spelling.split(" ")
        last = split[-1]
        replace = ""
        if "-" in last:
            lastSplit = last.split("-")
            lastWithDash = lastSplit[1]
            lastReplace = ""
            if lastWithDash in SpellingOfOrdinalNumbers.ordinalMap:
                lastReplace = SpellingOfOrdinalNumbers.ordinalMap[lastWithDash]
            elif lastWithDash.endswith("y"):
                lastReplace = lastWithDash[:-1] + "ieth"
            else:
                lastReplace = lastWithDash + "th"
            replace = lastSplit[0] + "-" + lastReplace
        else:
            if last in SpellingOfOrdinalNumbers.ordinalMap:
                replace = SpellingOfOrdinalNumbers.ordinalMap[last]
            elif last.endswith("y"):
                replace = last[:-1] + "ieth"
            else:
                replace = last + "th"
        split[-1] = replace
        return " ".join(split)

    nums = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    @staticmethod
    def numToString(n):
        return SpellingOfOrdinalNumbers.numToStringHelper(n)

    @staticmethod
    def numToStringHelper(n):
        if n < 0:
            return "negative " + SpellingOfOrdinalNumbers.numToStringHelper(-n)
        index = int(n)
        if n <= 19:
            return SpellingOfOrdinalNumbers.nums[index]
        if n <= 99:
            return SpellingOfOrdinalNumbers.tens[index // 10] + ("-" + SpellingOfOrdinalNumbers.numToStringHelper(n % 10) if n % 10 > 0 else "")
        label = None
        factor = 0
        if n <= 999:
            label = "hundred"
            factor = 100
        elif n <= 999999:
            label = "thousand"
            factor = 1000
        elif n <= 999999999:
            label = "million"
            factor = 1000000
        elif n <= 999999999999:
            label = "billion"
            factor = 1000000000
        elif n <= 999999999999999:
            label = "trillion"
            factor = 1000000000000
        elif n <= 999999999999999999:
            label = "quadrillion"
            factor = 1000000000000000
        else:
            label = "quintillion"
            factor = 1000000000000000000
        return SpellingOfOrdinalNumbers.numToStringHelper(n // factor) + " " + label + (" " + SpellingOfOrdinalNumbers.numToStringHelper(n % factor) if n % factor > 0 else "")