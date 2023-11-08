def lookAndSay(n):
    result = int("".join(str(len(list(group))) + digit for digit, group in itertools.groupby(str(n)))
    return result

def lookAndSay2(n):
    result = int("".join(str(len(list(group))) + digit for digit, group in itertools.groupby(str(n)))
    return result

def lookAndSay3(n):
    result = int("".join(str(len(list(group))) + digit for digit, group in itertools.groupby(str(n)))
    return result

def main():
    for i in range(10):
        print(lookAndSay(i))