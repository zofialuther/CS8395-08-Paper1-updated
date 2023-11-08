def test(inputList):
    if len(inputList) == 0:
        output = {}
    elif len(inputList) == 1:
        output = {inputList[0]}
    elif len(inputList) == 2:
        output = {inputList[0] + " and " + inputList[1]}
    else:
        output = ""
        for i in range(len(inputList) - 1):
            output += inputList[i] + ", "
        output += " and " + inputList[len(inputList) - 1]
    
    return True