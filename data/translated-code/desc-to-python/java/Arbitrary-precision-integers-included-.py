```python
import math

result = pow(5, pow(4, pow(3, 2)))
result_str = str(result)
print("First 20 digits:", result_str[:20])
print("Last 20 digits:", result_str[-20:])
print("Total number of digits:", len(result_str))
```