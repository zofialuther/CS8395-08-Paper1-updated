def exp_function(Base, Exp, Power):
    if Exp < 0:
        Power = 1 / (Base ** (Exp * -1))
    elif Exp > 0:
        Powers = [Base] * Exp
        Power = 1
        for i in range(Exp):
            Power = exp_folder(Base, Power, Powers[i], Power)
    else:
        Power = 1

def exp_folder(Base, Power, Powers, Result):
    Result = Base * Powers