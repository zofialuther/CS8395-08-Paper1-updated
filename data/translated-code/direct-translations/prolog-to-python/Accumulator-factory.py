from pyswip import Prolog, Functor, Variable

prolog = Prolog()

prolog.assertz(":- use_module(library(lambda)).")

prolog.assertz("define_g(N, G) :- "
               "    put_attr(V, user, N),"
               "    G = V +\\X^Y^(get_attr(V, user, N1),"
               "          Y is X + N1,"
               "          put_attr(V, user, Y)).")

prolog.assertz("accumulator :- "
               "    define_g(1, G),"
               "    format('Code of g : ~w~n', [G]),"
               "    call(G, 5, S),"
               "    writeln(S),"
               "    call(G, 2.3, R1),"
               "    writeln(R1).")

list(prolog.query("accumulator"))