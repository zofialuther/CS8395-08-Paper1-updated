def eval(inputs):
    if len(inputs) != 2:
        raise ValueError("IllegalArgumentException")
    return [XOR.eval(inputs[0], inputs[1]), AND.eval(inputs[0], inputs[1])]

def eval(inputs):
    if len(inputs) != 3:
        raise ValueError("IllegalArgumentException")
    haOutputs1 = HALF_ADDER.eval(inputs[0], inputs[1])
    haOutputs2 = HALF_ADDER.eval(haOutputs1[0], inputs[2])
    return [haOutputs2[0], OR.eval(haOutputs1[1], haOutputs2[1])]

def eval(inputs, numBits):
    if len(inputs) != (numBits << 1):
        raise ValueError("IllegalArgumentException")
    outputs = [False] * (numBits + 1)
    faOutputs = None
    for i in range(numBits):
        if faOutputs == None:
            faInputs[0] = False
        else:
            faInputs[0] = faOutputs[1]
        faInputs[1] = inputs[i]
        faInputs[2] = inputs[numBits + i]
        faOutputs = FULL_ADDER.eval(faInputs)
        outputs[i] = faOutputs[0]
    if faOutputs != None:
        outputs[numBits] = faOutputs[1]
    return outputs

def main(args):
    numBits = int(args[0])
    firstNum = int(args[1])
    secondNum = int(args[2])
    maxNum = 1 << numBits
    if firstNum < 0 or firstNum >= maxNum:
        print("First number is out of range")
        return
    if secondNum < 0 or secondNum >= maxNum:
        print("Second number is out of range")
        return
    multiBitAdder = buildAdder(numBits)
    inputs = [False] * (numBits << 1)
    firstNumDisplay = ""
    secondNumDisplay = ""
    for i in range(numBits):
        firstBit = ((firstNum >> i) & 1) == 1
        secondBit = ((secondNum >> i) & 1) == 1
        inputs[i] = firstBit
        inputs[numBits + i] = secondBit
        firstNumDisplay = ("1" if firstBit else "0") + firstNumDisplay
        secondNumDisplay = ("1" if secondBit else "0") + secondNumDisplay
    outputs = multiBitAdder.eval(inputs, numBits)
    outputNum = 0
    outputNumDisplay = ""
    outputCarryDisplay = None
    for i in range(numBits, -1, -1):
        outputNum = (outputNum << 1) | (1 if outputs[i] else 0)
        if i == numBits:
            outputCarryDisplay = "1" if outputs[i] else "0"
        else:
            outputNumDisplay += "1" if outputs[i] else "0"
    print("numBits=" + str(numBits))
    print("A=" + firstNumDisplay + " (" + str(firstNum) + "), B=" + secondNumDisplay + " (" + str(secondNum) + "), S=" + outputCarryDisplay + " " + outputNumDisplay + " (" + str(outputNum) + ")")