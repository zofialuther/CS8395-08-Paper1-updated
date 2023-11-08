from itertools import combinations

def minAbbrevnLength(words):
    if not words:
        return 0
    else:
        n = len(words)
        abbreviations = set()
        for i in range(1, n+1):
            for combo in combinations(words, i):
                abbreviation = ''.join(word[0] for word in combo)
                abbreviations.add(abbreviation)
        return len(min(abbreviations, key=len))

if __name__ == "__main__":
    with open("./weekDayNames.txt", "r") as file:
        lines = file.readlines()
        for line in lines[:10]:
            words = line.split()
            print(intercalate("\t", [str(minAbbrevnLength(words)), line]))