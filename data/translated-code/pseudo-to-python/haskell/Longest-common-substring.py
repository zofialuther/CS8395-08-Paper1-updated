def longestCommon(a, b):
    pair = (a, b)
    result = max([x for x in (pair[0][i:] for i in range(len(pair[0]))) if x in pair[1]], key=len)
    return result

def main():
    print(longestCommon("testing123testing", "thisisatest"))