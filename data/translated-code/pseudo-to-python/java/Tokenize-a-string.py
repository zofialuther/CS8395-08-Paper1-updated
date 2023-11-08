toTokenize = "Hello,How,Are,You,Today"
resultString = ""
tokenArray = toTokenize.split(",")
for element in tokenArray:
    resultString += element
    if element != tokenArray[-1]:
        resultString += "."
print(resultString)