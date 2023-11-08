inputString = "sample input string"
regexPattern = "sample regular expression pattern"

import re

pattern = re.compile(regexPattern)
matcher = pattern.finditer(inputString)

for match in matcher:
    print(match.group())