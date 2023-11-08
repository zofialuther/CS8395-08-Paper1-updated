from pyswip import Prolog

prolog = Prolog()
prolog.assertz("display_date :- get_time(T), format_time('~w', T, Date), format_time('~A, ~B ~d, ~Y', T, Date2), writeln(Date), writeln(Date2).")