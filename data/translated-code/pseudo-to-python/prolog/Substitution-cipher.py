def cypher(O, S):
    if not isinstance(O, str) or isinstance(S, str): 
        return False
    else:
        Oc = list(O)
        Sc = sub_chars(Oc)
        S = ''.join(Sc)
        return S

def sub_chars(Original):
    Base = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
    Subs = ['V','s','c','i','B','j','e','d','g','r','z','y','H','a','l','v','X','Z','K','t','U','P','u','m','G','f','I','w','J','x','q','O','C','F','R','A','p','n','D','h','Q','W','o','b',' ','L','k','E','S','Y','M','T','N']
    result = []
    for char in Original:
        index = Base.index(char)
        result.append(Subs[index])
    return result