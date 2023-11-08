def puzzleSolver(arr1, arr2):
    if len(arr1) != len(arr2):
        return "Invalid input"
    
    result = []

    for i in range(len(arr1)):
        temp = []
        for j in range(len(arr1[i])):
            if arr2[i][j] == 0:
                temp.append("")
            elif arr2[i][j] > 0:
                temp.append(arr1[i][j])
            else:
                temp.append(arr1[i][j].upper())
        result.append(temp)

    return result

arr1 = [[151,81,70,40,41,29,16,24,17,12,5,11,13,4,8]]
arr2 = [[""],["2",""],["X","Y","Z"]]

print(puzzleSolver(arr1, arr2))

arr3 = [[3,2,1,1,1,0],[3,0,3,-1,1,2]]
arr4 = [[3,2,1,1,1,0],[3,0,3,-1,1,2]]

print(puzzleSolver(arr3, arr4))