# Set operations and methods in Python

# Set union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2
print(union_set)

# Set intersection
intersection_set = set1 & set2
print(intersection_set)

# Set difference
difference_set = set1 - set2
print(difference_set)

# Set subset
subset_check = set1.issubset(set2)
print(subset_check)

# Set superset
superset_check = set1.issuperset(set2)
print(superset_check)

# Set equality
equality_check = set1 == set2
print(equality_check)

# Set membership
membership_check = 2 in set1
print(membership_check)

# Set non-membership
non_membership_check = 6 not in set1
print(non_membership_check)

# Set symmetric difference
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set)

# Set cardinality
cardinality = len(set1)
print(cardinality)

# Set mutability
set3 = {1, 2, 3}
set3.add(4)
print(set3)
set3.discard(2)
print(set3)
set3.update({5, 6})
print(set3)