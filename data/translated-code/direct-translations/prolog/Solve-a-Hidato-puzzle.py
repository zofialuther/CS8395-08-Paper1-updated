from pyswip import Prolog

prolog = Prolog()

prolog.assertz("init1(Li) :- Li = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, A, 33, 35, B, C, 0, 0, 0, 0, 0, D, E, 24, 22, F, 0, 0, 0, 0, 0, G, H, I, 21, J, K, 0, 0, 0, 0, 0, L, 26, M, 13, 40, 11, 0, 0, 0, 0, 27, N, O, P, 9, Q, 1, 0, 0, 0, 0, 0, 0, R, S, 18, T, U, 0, 0, 0, 0, 0, 0, V, 7, W, X, 0, 0, 0, 0, 0, 0, 0, 5, Y, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]")
prolog.assertz("hidato :- init1(Li), init2(1, 1, 10, Li), my_write(Li).")
prolog.assertz("init2(_N, Col, Max_Col, _L) :- Col is Max_Col - 1.")
prolog.assertz("init2(N, Lig, Col, L) :- I is N + Lig * Col, nth0(I, L, 0), !, V is N+1, (V > Col -> N1 = 1, Lig1 is Lig + 1; N1 = V, Lig1 = Lig), init2(N1, Lig1, Col, L).")
prolog.assertz("init2(1, Lig, Col, L) :- init2(2, Lig, Col, L).")
prolog.assertz("init2(Col, Lig, Col, L) :- Lig1 is Lig+1, init2(1, Lig1, Col, L).")
prolog.assertz("init2(N, Lig, Col, L) :- I is N + Lig * Col, nth0(I, L, V), I1 is I  - 1, I2 is I  + 1, I3 is I  - Col, I4 is I  + Col, I5 is I3 - 1, I6 is I3 + 1, I7 is I4 - 1, I8 is I4 + 1, compute_BI(L, V, [I1,I2,I3,I4,I5,I6,I7,I8], VI, BI), sum(BI, #=, SBI), ((V #=  1 #\/ V #=  40) #/\ SBI #= 1) #\/ (V #\= 1 #/\ V #\= 40  #/\ SBI #= 2) #<==> 1, labeling([ffc, enum], [V | VI]), N1 is N+1, init2(N1, Lig, Col, L).")
prolog.assertz("compute_BI(L, V, I, VI, BI) :- nth0(I, L, VI), (VI #= 0 #==> BI #= 0), (VI #\= 0 #/\ (V - VI #= 1 #\/ VI - V #= 1))  #<==> BI.")
prolog.assertz("my_write([0, A, B, C, D, E, F, G, H, 0 | T]) :- maplist(my_write_1, [A, B, C, D, E, F, G, H]), nl, my_write(T).")
prolog.assertz("my_write_1(0) :- write('   ').")
prolog.assertz("my_write_1(X) :- writef('%3r', [X]).")

list(prolog.query("hidato."))