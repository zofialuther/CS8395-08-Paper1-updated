```python
from pyswip import Prolog

prolog = Prolog()

prolog.assertz("numlist(N,N,[])")
prolog.assertz("numlist(M,N,[M|L]) :- M < N, M1 is M+1, numlist(M1, N, L)")

prolog.assertz("pangram(L) :- numlist(97, 123, Alphabet), forall(member(X, Alphabet), member(X, L))")

prolog.assertz("format('~s is a pangram: ~t~w~n', [L, Result]) :- pangram(L), Result = true")
prolog.assertz("format('~s is not a pangram: ~t~w~n', [L, Result]) :- \+pangram(L), Result = false")

pangram_example = "pangram_example :- L1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'], L2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']"

prolog.assertz(pangram_example)

list(prolog.query("pangram_example"))
```