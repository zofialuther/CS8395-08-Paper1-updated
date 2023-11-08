from lambda import exclude

def stripchars(String, Exclude, Result):
    Result1 = exclude(String, Exclude)
    Result = ''.join(Result1)