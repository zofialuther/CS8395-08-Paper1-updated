def average(x):
    if x:
        return sum(x) / len(x)
    else:
        return 0

print(average([0,0,3,1,4,1,5,9,0,0]))
print(average([1e20,-1e-20,3,1,4,1,5,9,-1e20,1e-20]))