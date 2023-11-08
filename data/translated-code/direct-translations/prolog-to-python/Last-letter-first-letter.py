from pyswip import Prolog

prolog = Prolog()

prolog.assertz("res(0, 0, [])")

def last_first():
    prolog.retractall("res(_,_,_)")
    prolog.assertz("res(0, 0, [])")
    res = list(prolog.query("res(Len, Nb, L1), maplist(\X^Y^(X = [Y, _, _]), L1, L)"))
    return res[0]["Len"], res[0]["Nb"], res[0]["L"]

def last_first_aux():
    L = ["audino", "bagon", "baltoy", "banette", "bidoof", "braviary", "bronzor",
         "carracosta", "charmeleon", "cresselia", "croagunk", "darmanitan", "deino",
         "emboar", "emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus",
         "heatmor", "heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan",
         "kricketune", "landorus", "ledyba", "loudred", "lumineon", "lunatone",
         "machamp", "magnezone", "mamoswine", "nosepass", "petilil", "pidgeotto",
         "pikachu", "pinsir", "poliwrath", "poochyena", "porygon2", "porygonz",
         "registeel", "relicanth", "remoraid", "rufflet", "sableye", "scolipede",
         "scrafty", "seaking", "sealeo", "silcoon", "simisear", "snivy", "snorlax",
         "spoink", "starly", "tirtouga", "trapinch", "treecko", "tyrogue", "vigoroth",
         "vulpix", "wailord", "wartortle", "whismur", "wingull", "yamask"]
    for Word in L:
        last_first_aux_recur([Word], [w for w in L if w != Word])

def last_first_aux_recur(L, Rest):
    if not lance_p([L[0]] + Rest):
        last_first_aux_recur([Rest[0]] + L, Rest[1:])

def lance_p(L):
    LF = list(prolog.query("p(LF, L)"))
    Len = LF[0]["Len"]
    Nb = LF[0]["Nb"]
    Lst = LF[0]["Lst"]
    if len(LF[0]["LF"]) > 0:
        prolog.retract("res(Len, Nb, Lst)")
        Len1 = len(LF[0]["LF"])
        if Len1 > Len:
            prolog.assertz("res({}, 1, {})".format(Len1, LF[0]["LF"]))
        elif Len1 == Len:
            Nb1 = Nb + 1
            prolog.assertz("res({}, {}, {})".format(Len, Nb1, Lst))

def init(L):
    L0 = ["audino", "bagon", "baltoy", "banette", "bidoof", "braviary", "bronzor",
         "carracosta", "charmeleon", "cresselia", "croagunk", "darmanitan", "deino",
         "emboar", "emolga", "exeggcute", "gabite", "girafarig", "gulpin", "haxorus",
         "heatmor", "heatran", "ivysaur", "jellicent", "jumpluff", "kangaskhan",
         "kricketune", "landorus", "ledyba", "loudred", "lumineon", "lunatone",
         "machamp", "magnezone", "mamoswine", "nosepass", "petilil", "pidgeotto",
         "pikachu", "pinsir", "poliwrath", "poochyena", "porygon2", "porygonz",
         "registeel", "relicanth", "remoraid", "rufflet", "sableye", "scolipede",
         "scrafty", "seaking", "sealeo", "silcoon", "simisear", "snivy", "snorlax",
         "spoink", "starly", "tirtouga", "trapinch", "treecko", "tyrogue", "vigoroth",
         "vulpix", "wailord", "wartortle", "whismur", "wingull", "yamask"]
    prolog.assertz("init_(W, [W, F, L]) :- first_letter(W, F), last_letter(W, L).")
    prolog.assertz("first_letter(A, F) :- atom_chars(A, [F | _]).")
    prolog.assertz("last_letter(A, L) :- atom_chars(A, LC), reverse(LC, [L | _]).")
    prolog.assertz("p0([_, _, W], [_, W, _]).")
    prolog.assertz("p([A | T], [A | L]) :- select(B, L, L1), p0(A,B), T = [B | T1], p([B | T1], [B | L1]).")
    prolog.assertz("p([_], _).")
    map(lambda w: prolog.assertz("init_(" + w + ", [" + w + ", " + first_letter(w) + ", " + last_letter(w) + "])."), L0)

Len, Nb, L = last_first()
print(Len, Nb, L)