```python
from Data.List import *

s3 = list(set([1,2,3,4,3]))
print(s3)

s4 = [3,4,5,6]

union_list = list(set(s3) | set(s4))
print(union_list)

intersection_list = list(set(s3) & set(s4))
print(intersection_list)

difference_list = list(set(s3) - set(s4))
print(difference_list)

new_s3 = [42] + s3
print(new_s3)

s3.remove(3)
new_s3 = s3
print(new_s3)
```