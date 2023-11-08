def main():
    args = getArgs()
    if len(args) != 1:
        print("Please provide exactly one source file as an argument.")
        return
    sourcePath = args[0]
    source = readFile(sourcePath)
    input = getContents()
    result = markovParser(sourcePath, source)
    if result.isRight():
        print(runMarkov(result.rules, input))
    else:
        print("Parse error at " + str(result.error))

class Rule:
    def __init__(self, from, terminating, to):
        self.from = from
        self.terminating = terminating
        self.to = to

def markovParser(sourcePath, source):
    return liftM(catMaybes, (comment() | rule()).sepEndBy(many1(newline)))

def comment():
    char('#') & skipMany(nonnl) & return Nothing

def rule():
    return liftM(Just, liftM3(Rule, manyTill(nonnl, arrow()), succeeds(char('.')), many(nonnl)))

def arrow():
    ws() & string("->") & ws()

def nonnl():
    noneOf("\n")

def ws():
    return many1(oneOf(" \t"))

def succeeds(p):
    return option(False, p) & return True

def runMarkov(rules, s):
    if not rules:
        return s
    else:
        from, terminating, to = rules[0]
        if g("", s) == "":
            return f(rules[1:], s)
        else:
            ahead = g("", s)
            if from in ahead:
                new = ahead.replace(from, to)
                if terminating:
                    return new
                else:
                    return f(rules, new)
            else:
                return g(a + [before], as)