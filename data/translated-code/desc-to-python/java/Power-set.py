def generatePowerSet(arr, length, result):
    if length == 0:
        result.append("")
        return result
    result = generatePowerSet(arr, length-1, result)
    temp = []
    for i in result:
        temp.append(i + arr[length-1])
    result.extend(temp)
    return result