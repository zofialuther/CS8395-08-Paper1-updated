# Import the TreeSet class from the java.util package
from java.util import TreeSet

# Create four TreeSet objects
set1 = TreeSet()
set2 = TreeSet()
set3 = TreeSet()
set4 = TreeSet()

# Populate the sets with integer values
set1.add(1)
set1.add(2)
set1.add(3)

set2.add(3)
set2.add(4)
set2.add(5)

set3.add(1)
set3.add(3)
set3.add(5)

set4.add(6)
set4.add(7)
set4.add(8)

# Perform set operations
union_set = TreeSet(set1)
union_set.addAll(set2)

difference_set = TreeSet(set1)
difference_set.removeAll(set3)

intersection_set = TreeSet(set1)
intersection_set.retainAll(set2)

# Check for subsets and equality between sets
is_subset = set3.containsAll(set1)
is_equal = set1.equals(set2)

# Create an empty and immutable set
empty_set = TreeSet()
immutable_set = TreeSet(set1)
immutable_set = Collections.unmodifiableSet(immutable_set)

# Test for emptiness
is_empty = empty_set.isEmpty()

# Check for common elements between sets
common_elements = TreeSet(set1)
common_elements.retainAll(set3)