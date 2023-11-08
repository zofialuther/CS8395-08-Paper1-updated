```python
import re

def main():
    rules = read_rules("markov_rules.txt")
    tests = read_tests("markov_tests.txt")

    pattern = re.compile(r'^([^#]*?)\s+->\s+(\.?)(.*)')

    for test in tests:
        orig_test = test

        captures = []
        for rule in rules[tests.index(test)]:
            m = re.match(pattern, rule)
            if m:
                groups = m.groups()
                captures.append(groups)

        copy = test
        for c in captures:
            test = test.replace(c[0], c[2])
            if c[1] == ".":
                break
            if test != copy:
                captures = []
                copy = test

        print(f"{orig_test}\n{test}\n")

def read_tests(path):
    with open(path, 'r') as file:
        return file.readlines()

def read_rules(path):
    with open(path, 'r') as file:
        return [line.split() for line in file.read().split('\n\n')]

if __name__ == "__main__":
    main()
```