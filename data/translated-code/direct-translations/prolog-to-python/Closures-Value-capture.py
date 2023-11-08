from pyswip import Prolog, Functor

prolog = Prolog()
prolog.consult("lambda")

def make_func(I):
    return Functor("/", "X", Functor("is", "X", Functor("*", I, I)))

def call_func(N, F):
    R = list(prolog.query(call(F, R)))[0]["R"]
    print(f"Func {N} : {R}")

Lnum = list(range(1, 11))
Lfunc = list(map(make_func, Lnum))

for i in range(len(Lnum)):
    call_func(Lnum[i], Lfunc[i])