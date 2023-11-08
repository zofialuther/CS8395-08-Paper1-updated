from prologdef import declare, clause, predicate

declare('system:set_prolog_flag(double_quotes,chars)')

@predicate
def repeat(SOURCEz0, COUNT0, TARGETz):
    clause('prolog:phrase(repeat(SOURCEz0,COUNT0),TARGETz)')

@predicate
def repeat(SOURCEz0, 0):
    clause('!', ', []')

@predicate
def repeat(SOURCEz0, COUNT0):
    clause('SOURCEz0 , { COUNT is COUNT0 - 1 } , repeat(SOURCEz0,COUNT)')