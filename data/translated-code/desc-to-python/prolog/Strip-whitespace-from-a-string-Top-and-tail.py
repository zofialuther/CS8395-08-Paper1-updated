```python
# Python code

# Define Prolog flag to use double quotes as character codes
:- set_prolog_flag(double_quotes, codes).

% Define predicates to strip leading, trailing, and both leading and trailing spaces
strip_leading([32|T], R) :- strip_leading(T, R).
strip_leading(R, R).

strip_trailing(L, R) :- reverse(L, Rev), strip_leading(Rev, R1), reverse(R1, R).

strip_leading_and_trailing(L, R) :- strip_leading(L, R1), strip_trailing(R1, R).

% Define DCG rules for stripping spaces and non-spaces
strip_spaces --> " ", strip_spaces.
strip_spaces --> [X], {X \= 32}, strip_spaces.
strip_spaces --> [].
```