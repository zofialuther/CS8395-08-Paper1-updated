def dotp(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of equal length")
    
    result = 0
    for i in range(len(list1)):
        result += list1[i] * list2[i]
    
    return result

def main():
    vector1 = [1, 2, 3]
    vector2 = [1, 1, 1]
    result = dotp(vector1, vector2)
    print(result)

main()