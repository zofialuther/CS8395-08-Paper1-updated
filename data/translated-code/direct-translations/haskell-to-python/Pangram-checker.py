from string import ascii_lowercase

def pangram(s):
    return not bool(set(ascii_lowercase) - set(s.lower()))

print(pangram("How razorback-jumping frogs can level six piqued gymnasts!"))