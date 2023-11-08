```python
class GateLogic:
    # Basic gate interfaces
    class OneInputGate:
        def eval(self, input):
            pass

    class TwoInputGate:
        def eval(self, input1, input2):
            pass

    class MultiGate:
        def eval(self, *inputs):
            pass

    # Create NOT
    NOT = OneInputGate()
    def NOT_eval(self, input):
        return not input
    NOT.eval = NOT_eval

    # Create AND
    AND = TwoInputGate()
    def AND_eval(self, input1, input2):
        return input1 and input2
    AND.eval = AND_eval

    # Create OR
    OR = TwoInputGate()
    def OR_eval(self, input1, input2):
        return input1 or input2
    OR.eval = OR_eval

    # Create XOR
    XOR = TwoInputGate()
    def XOR_eval(self, input1, input2):
        return self.OR.eval(self.AND.eval(input1, self.NOT.eval(input2)), self.AND.eval(self.NOT.eval(input1), input2))
    XOR.eval = XOR_eval

    # Create HALF_ADDER
    HALF_ADDER = MultiGate()
    def HALF_ADDER_eval(self, *inputs):
        if len(inputs) != 2:
            raise ValueError
        return [self.XOR.eval(inputs[0], inputs[1]), self.AND.eval(inputs[0], inputs[1])]
    HALF_ADDER.eval = HALF_ADDER_eval

    # Create FULL_ADDER
    FULL_ADDER = MultiGate()
    def FULL_ADDER_eval(self, *inputs):
        if len(inputs) != 3:
            raise ValueError
        haOutputs1 = self.HALF_ADDER.eval(inputs[0], inputs[1])
        haOutputs2 = self.HALF_ADDER.eval(haOutputs1[0], inputs[2])
        return [haOutputs2[0], self.OR.eval(haOutputs1[1], haOutputs2[1])]
    FULL_ADDER.eval = FULL_ADDER_eval

    @staticmethod
    def buildAdder(numBits):
        def eval(self, *inputs):
            if len(inputs) != (numBits << 1):
                raise ValueError
            outputs = [False] * (numBits + 1)
            faInputs = [False] * 3
            faOutputs = None
            for i in range(numBits):
                faInputs[0] = False if faOutputs is None else faOutputs[1]
                faInputs[1] = inputs[i]
                faInputs[2] = inputs[numBits + i]
                faOutputs = self.FULL_ADDER.eval(*faInputs)
                outputs[i] = faOutputs[0]
            if faOutputs is not None:
                outputs[numBits] = faOutputs[1]
            return outputs
        return type('adder', (GateLogic.MultiGate,), {'eval': eval})

    @staticmethod
    def main(args):
        numBits = int(args[0])
        firstNum = int(args[1])
        secondNum = int(args[2])
        maxNum = 1 << numBits
        if (firstNum < 0) or (firstNum >= maxNum):
            print("First number is out of range")
            return
        if (secondNum < 0) or (secondNum >= maxNum):
            print("Second number is out of range")
            return
        multiBitAdder = GateLogic.buildAdder(numBits)()
        inputs = [False] * (numBits << 1)
        firstNumDisplay = ''
        secondNumDisplay = ''
        for i in range(numBits):
            firstBit = ((firstNum >> i) & 1) == 1
            secondBit = ((secondNum >> i) & 1) == 1
            inputs[i] = firstBit
            inputs[numBits + i] = secondBit
            firstNumDisplay = ('1' if firstBit else '0') + firstNumDisplay
            secondNumDisplay = ('1' if secondBit else '0') + secondNumDisplay
        outputs = multiBitAdder.eval(*inputs)
        outputNum = 0
        outputNumDisplay = ''
        outputCarryDisplay = None
        for i in range(numBits, -1, -1):
            outputNum = (outputNum << 1) | (1 if outputs[i] else 0)
            if i == numBits:
                outputCarryDisplay = '1' if outputs[i] else '0'
            else:
                outputNumDisplay += '1' if outputs[i] else '0'
        print("numBits=" + str(numBits))
        print("A=" + firstNumDisplay + " (" + str(firstNum) + "), B=" + secondNumDisplay + " (" + str(secondNum) + "), S=" + outputCarryDisplay + " " + outputNumDisplay + " (" + str(outputNum) + ")")
```