def showMat(mat):
    result = ""
    for row in mat:
        line = ""
        for element in row:
            line = line + " " + str(element)
        result = result + line + "\n"
    return result