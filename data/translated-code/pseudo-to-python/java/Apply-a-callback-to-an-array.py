myIntArray = [1, 2, 3, 4, 5]
sum = 0
for element in myIntArray:
    cube = element * element * element
    print(cube)
    sum = sum + cube
print("sum: " + str(sum))