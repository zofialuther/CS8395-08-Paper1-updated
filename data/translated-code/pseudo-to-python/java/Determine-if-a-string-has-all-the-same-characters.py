text = "This is a sample text with some numbers like 12345 and 67890"
patternString = r'\d+'

pattern = re.compile(patternString)
matcher = pattern.finditer(text)

for match in matcher:
    print(match.group())

