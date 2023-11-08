def flatten(nl):
    return flatten_(nl, [])

def flatten_(nl, cont):
    if isinstance(nl, Entry):
        return cont.append(nl.value)
    elif isinstance(nl, NList):
        return foldr(flatten_, cont, nl.entries)