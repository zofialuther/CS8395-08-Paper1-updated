def transpose(In):
    Out = []
    for i in range(len(In[0])):
        temp = []
        for row in In:
            temp.append(row[i])
        Out.append(temp)
    return Out

# Example usage
input_matrix = [[1,2,3,4], [5,6,7,8]]
output_matrix = transpose(input_matrix)
print(output_matrix)  # Output: [[1, 5], [2, 6], [3, 7], [4, 8]]