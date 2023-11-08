```python
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("list_to_ord_set([1,2,3,4], A), list_to_ord_set([2,4,6,8], B).")
prolog.assertz("ord_memberchk(2, A).")
prolog.assertz("ord_union(A, B, Union).")
prolog.assertz("ord_intersection(A, B, Intersection).")
prolog.assertz("ord_subtract(A, B, Diff).")
prolog.assertz("ord_subset([2,4], B).")
prolog.assertz("A == [1,2,3,4].")
prolog.assertz("ord_propsubset(A, B) :- ord_subset(A, B), \\+(A == B).")
prolog.assertz("ord_add_element(A, 19, NewA).")
prolog.assertz("ord_del_element(NewA, 3, NewerA).")

for result in prolog.query("A = [1, 2, 3, 4], B = [2, 4, 6, 8]."):
    print(result["A"], result["B"])

for result in prolog.query("ord_memberchk(2, A)."):
    print(result)

for result in prolog.query("ord_union(A, B, Union)."):
    print(result["Union"])

for result in prolog.query("ord_intersection(A, B, Intersection)."):
    print(result["Intersection"])

for result in prolog.query("ord_subtract(A, B, Diff)."):
    print(result["Diff"])

for result in prolog.query("ord_subset(A, B)."):
    print(result)

for result in prolog.query("ord_subset([2,4], B)."):
    print(result)

for result in prolog.query("A == B."):
    print(result)

for result in prolog.query("A == [1,2,3,4]."):
    print(result)

for result in prolog.query("ord_propsubset(A, B)."):
    print(result)

for result in prolog.query("ord_add_element(A, 19, NewA)."):
    print(result["NewA"])

for result in prolog.query("ord_del_element(NewA, 3, NewerA)."):
    print(result["NewerA"])
```