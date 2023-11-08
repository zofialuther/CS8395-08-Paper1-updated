from typing import List
import sys
import re

class Rule:
    def __init__(self, from_str: str, terminating: bool, to_str: str):
        self.from_str = from_str
        self.terminating = terminating
        self.to_str = to_str

def markov_parser(s: str) -> List[Rule]:
    rules = []
    lines = s.split("\n")
    for line in lines:
        if not line.startswith("#") and "->" in line:
            parts = line.split("->")
            from_str = parts[0].strip()
            to_str = parts[1].strip()
            terminating = to_str.endswith(".")
            if terminating:
                to_str = to_str[:-1]
            rule = Rule(from_str, terminating, to_str)
            rules.append(rule)
    return rules

def run_markov(rules: List[Rule], s: str) -> str:
    for rule in rules:
        s = re.sub(rule.from_str, rule.to_str, s)
        if rule.terminating:
            break
    return s

def main():
    args = sys.argv
    if len(args) != 2:
        print("Please provide exactly one source file as an argument.")
        sys.exit(1)
    source_path = args[1]
    with open(source_path, "r") as file:
        source = file.read()
    input_str = sys.stdin.read()
    rules = markov_parser(source)
    result = run_markov(rules, input_str)
    print(result)

if __name__ == "__main__":
    main()