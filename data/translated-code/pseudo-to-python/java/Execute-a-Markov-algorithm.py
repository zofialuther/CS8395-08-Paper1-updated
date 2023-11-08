def main(args):
    rules = readRules("markov_rules.txt")
    tests = readTests("markov_tests.txt")
    pattern = re.compile(r"^([^#]*?)\s+->\s+(\.?)(.*)")

    for i in range(len(tests)):
        origTest = tests[i]
        captures = []

        for rule in rules[i]:
            m = re.match(pattern, rule)
            if m:
                groups = [m.group(j) for j in range(1, m.lastindex + 1)]
                captures.append(groups)

        test = origTest
        copy = test
        j = 0
        while j < len(captures):
            c = captures[j]
            test = test.replace(c[0], c[2])
            if c[1] == ".":
                break
            if test != copy:
                j = -1  # redo loop
                copy = test
            j += 1

        print(origTest)
        print(test)

def readTests(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.readlines()

def readRules(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.read()
        rules = [rule.split('\n') for rule in lines.split('\n\n')]
        return rules