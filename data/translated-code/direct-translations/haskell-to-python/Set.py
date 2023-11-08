import Data.List

s3 = list(set([1,2,3,4,3])) # Remove duplicates from list
print(s3)

s4 = [3,4,5,6]
print(list(set(s3 + s4))) # Union

print(list(set(s3) & set(s4)) # Intersection

print(list(set(s3) - set(s4)) # Difference

print([42] + s3) # Return new list with element inserted at the beginning

s3.remove(3) # Return new list with first occurrence of element removed
print(s3)