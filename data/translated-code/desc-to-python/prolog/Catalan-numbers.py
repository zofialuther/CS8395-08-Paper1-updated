```python
catalan(N) :-
    numlist(0, N, Numbers),
    maplist(calculate_catalan, Numbers, CatalanValues),
    maplist(my_write, Numbers, CatalanValues).

calculate_catalan(N, Value) :-
    init(N, Value, _).

my_write(Number, Value) :-
    format("~w : ~w~n", [Number, Value]).
```