```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz("set_prolog_flag(double_quotes, chars).")

prolog.assertz("repeat(Source, Count, Output) :- string_chars(Source, Chars), string_chars(Output, Repeated), repeat_chars(Chars, Count, Repeated).")

prolog.assertz("repeat_chars(_, 0, '').")
prolog.assertz("repeat_chars(Chars, Count, Repeated) :- Count > 0, NewCount is Count - 1, repeat_chars(Chars, NewCount, Temp), string_concat(Chars, Temp, Repeated).")
```