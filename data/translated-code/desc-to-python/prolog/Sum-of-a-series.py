```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("sum_of_reciprocals.pl")

result = list(prolog.query("sum(S)"))
print(result[0]['S'])
```