def collapse(in_string):
    result = ""
    for i in range(len(in_string)):
        if i == 0 or in_string[i-1] != in_string[i]:
            result += in_string[i]
    return result

if __name__ == "__main__":
    test_strings = [
        "",
        "\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ",
        "..1111111111111111111111111111111111111111111111111111111111111117777888",
        "I never give 'em hell, I just tell the truth, and they think it's hell. ",
        "                                                    --- Harry S Truman  ",
        "122333444455555666666777777788888888999999999",
        "The better the 4-wheel drive, the further you'll be from help when ya get stuck!",
        "headmistressship"
    ]

    for s in test_strings:
        result = collapse(s)
        print(f"old:  {len(s)} <<<{s}>>>\nnew:  {len(result)} <<<{result}>>>\n")