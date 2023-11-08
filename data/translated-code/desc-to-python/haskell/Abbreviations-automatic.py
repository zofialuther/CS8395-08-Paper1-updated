def minAbbrevnLength(strings):
    def allAbbrevs(s, prefix):
        if not s:
            return [prefix]
        return allAbbrevs(s[1:], prefix + s[0]), allAbbrevs(s[1:], prefix)
    
    abbrevs = set()
    for s in strings:
        abbrevs.update(allAbbrevs(s, ""))
        
    for i in range(1, len(strings[0])):
        if all(len(s[:i]) in abbrevs for s in strings):
            return i

with open('input.txt', 'r') as file:
    strings = [file.readline().strip() for _ in range(10)]

print(minAbbrevnLength(strings))