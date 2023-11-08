def squeeze(in, include):
    sb = ""
    for i in range(len(in)):
        if i == 0 or in[i-1] != in[i] or (in[i-1] == in[i] and in[i] != include):
            sb += in[i]
    return sb

testStrings = [
    "",
    "\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ",
    "..1111111111111111111111111111111111111111111111111111111111111117777888",
    "I never give 'em hell, I just tell the truth, and they think it's hell. ",
    "                                                    --- Harry S Truman  ",
    "122333444455555666666777777788888888999999999",
    "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
    "headmistressship"
]

testChar = [
    " ",
    "-",
    "7",
    ".",
    " -r",
    "5",
    "e",
    "s"
]

for testNum in range(len(testStrings)):
    s = testStrings[testNum]
    for c in testChar[testNum]:
        result = squeeze(s, c)
        print(f"use: '{c}'\nold:  {len(s)} <<<{s}>>>\nnew:  {len(result)} <<<{result}>>>\n")