def foldr(Foldy, Items, Starter, AccUp):
    if len(Items) > 0:
        AccUpPrev = foldr(Foldy, Items[1:], Starter, AccUp) # recurse
        AccUp = Foldy(Items[0], AccUpPrev) # call Foldy as last action
    else:
        AccUp = Starter # bounce Starter "upwards" into AccUp
    return AccUp