from functools import partial

def fix(f):
    return partial(f, fix(f))

fix(print)("SPAM")