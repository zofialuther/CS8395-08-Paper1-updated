```python
class StateTapeSymbolPair:
    def __init__(self, state, tapeSymbol):
        self.state = state
        self.tapeSymbol = tapeSymbol

    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + (0 if self.state is None else hash(self.state))
        result = prime * result + (0 if self.tapeSymbol is None else hash(self.tapeSymbol))
        return result

    def __eq__(self, other):
        if self == other:
            return True
        if other is None or self.__class__ != other.__class__:
            return False
        if self.state is None:
            if other.state is not None:
                return False
        elif self.state != other.state:
            return False
        if self.tapeSymbol is None:
            if other.tapeSymbol is not None:
                return False
        elif self.tapeSymbol != other.tapeSymbol:
            return False
        return True

    def __str__(self):
        return "(" + self.state + "," + self.tapeSymbol + ")"


class Transition:
    def __init__(self, fromState, toState, direction):
        self.fromState = fromState
        self.toState = toState
        self.direction = direction

    def __str__(self):
        return str(self.fromState) + "=>" + str(self.toState) + "/" + str(self.direction)


class UTM:
    def __init__(self, transitions, terminalStates, initialState, blankSymbol):
        self.blankSymbol = blankSymbol
        self.transitions = {}
        for t in transitions:
            self.transitions[t.fromState] = t
        self.terminalStates = terminalStates
        self.initialState = initialState
        self.tape = []
        self.head = None

    def initializeTape(self, input):
        self.tape = list(input)

    def runTM(self):
        if len(self.tape) == 0:
            self.tape.append(self.blankSymbol)

        self.head = iter(self.tape)
        next(self.head)
        prev = self.head

        tsp = StateTapeSymbolPair(self.initialState, self.tape[0])

        while tsp in self.transitions:
            trans = self.transitions[tsp]
            prevVal = next(self.head, None)
            if prevVal is None:
                self.tape.append(self.blankSymbol)
                self.head = iter(self.tape)
                next(self.head)
                prev = self.head
            else:
                prev = prevVal
                next(self.head)

            if trans.direction == -1:
                if prev is None:
                    self.tape.insert(0, self.blankSymbol)
                    self.head = iter(self.tape)
                else:
                    prev, prev = prev
            elif trans.direction == 1:
                if prev is None:
                    self.tape.append(self.blankSymbol)
                    self.head = iter(self.tape)
                    prev = next(self.head)
                else:
                    next(self.head)
                    prev, prev = prev
            else:
                prev = trans.toState.tapeSymbol

            tsp.state = trans.toState.state

        if tsp.state in self.terminalStates:
            return self.tape
        else:
            return None

    def __str__(self):
        try:
            headPos = self.tape.index(next(self.head))
            s = "[ "
            s += " ".join(self.tape[:headPos]) + " [H] " + " ".join(self.tape[headPos:])
            return s + "]"
        except Exception as e:
            return ""

    @staticmethod
    def main():
        # Your main method code here
```