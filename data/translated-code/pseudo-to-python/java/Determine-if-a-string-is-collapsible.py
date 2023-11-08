def collapse(input):
    sb = ""
    for i in range(len(input)):
        if i == 0 or input[i-1] != input[i]:
            sb += input[i]
    return sb

def main():
    strings = ["", "\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ", "..1111111111111111111111111111111111111111111111111111111111111117777888", "I never give 'em hell, I just tell the truth, and they think it's hell. ", " --- Harry S Truman  ", "122333444455555666666777777788888888999999999", "The better the 4-wheel drive, the further you'll be from help when ya get stuck!", "headmistressship"]
    for s in strings:
        result = collapse(s)
        print(f"old: {len(s):2d} <<<{s}>>>\nnew: {len(result):2d} <<<{result}>>>\n\n")