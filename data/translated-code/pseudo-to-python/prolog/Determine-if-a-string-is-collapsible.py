def collapse_(inputList, outputList):
    if len(inputList) == 0:
        outputList = []
    elif len(inputList) == 1:
        outputList = [inputList[0]]
    elif inputList[0] == inputList[1]:
        outputList = collapse_([inputList[0], *inputList[2:]], outputList)
    else:
        outputList = [inputList[0], *collapse_([inputList[1], *inputList[2:]], outputList)]

def collapse(inputStr, outputCollapsed):
    inputChars = list(inputStr)
    result = []
    collapse_(inputChars, result)
    outputCollapsed = ''.join(result)