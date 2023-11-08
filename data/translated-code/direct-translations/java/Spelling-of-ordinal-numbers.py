```python
class SpellingOfOrdinalNumbers:
    ordinalMap = {
        "one": "first",
        "two": "second",
        "three": "third",
        "five": "fifth",
        "eight": "eighth",
        "nine": "ninth",
        "twelve": "twelfth"
    }

    nums = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    @staticmethod
    def to_ordinal(n):
        spelling = SpellingOfOrdinalNumbers.num_to_string(n)
        split = spelling.split(" ")
        last = split[-1]
        replace = ""
        if "-" in last:
            last_split = last.split("-")
            last_with_dash = last_split[1]
            if last_with_dash in SpellingOfOrdinalNumbers.ordinalMap:
                last_replace = SpellingOfOrdinalNumbers.ordinalMap[last_with_dash]
            elif last_with_dash.endswith("y"):
                last_replace = last_with_dash[:-1] + "ieth"
            else:
                last_replace = last_with_dash + "th"
            replace = last_split[0] + "-" + last_replace
        else:
            if last in SpellingOfOrdinalNumbers.ordinalMap:
                replace = SpellingOfOrdinalNumbers.ordinalMap[last]
            elif last.endswith("y"):
                replace = last[:-1] + "ieth"
            else:
                replace = last + "th"
        split[-1] = replace
        return " ".join(split)

    @staticmethod
    def num_to_string(n):
        return SpellingOfOrdinalNumbers.num_to_string_helper(n)

    @staticmethod
    def num_to_string_helper(n):
        if n < 0:
            return "negative " + SpellingOfOrdinalNumbers.num_to_string_helper(-n)
        index = int(n)
        if n <= 19:
            return SpellingOfOrdinalNumbers.nums[index]
        if n <= 99:
            return SpellingOfOrdinalNumbers.tens[index // 10] + ("-" + SpellingOfOrdinalNumbers.num_to_string_helper(n % 10) if n % 10 > 0 else "")
        labels = ["hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]
        factors = [100, 1000, 1000000, 1000000000, 1000000000000, 1000000000000000, 1000000000000000000]
        for label, factor in zip(labels, factors):
            if n <= factor:
                return SpellingOfOrdinalNumbers.num_to_string_helper(n // factor) + " " + label + (" " + SpellingOfOrdinalNumbers.num_to_string_helper(n % factor) if n % factor > 0 else "")
```