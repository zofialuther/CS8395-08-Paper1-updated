def amb(E, ES):
    if E in ES:
        return True
    else:
        if ES:
            return amb(E, ES[1:])
        else:
            return False

def joins(Left, Right):
    if Left[-1] != Right[0]:
        return False
    else:
        return True

def amb_example():
    words = ["the","that","a"], ["frog","elephant","thing"], ["walked","treaded","grows"], ["slowly","quickly"]
    for w1 in words[0]:
        for w2 in words[1]:
            for w3 in words[2]:
                for w4 in words[3]:
                    if joins(w1, w2) and joins(w2, w3) and joins(w3, w4):
                        return [w1, w2, w3, w4]