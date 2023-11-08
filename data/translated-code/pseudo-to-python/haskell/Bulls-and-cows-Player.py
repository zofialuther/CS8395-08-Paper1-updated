def combinationsOf(k, lst):
    if k == 0:
        return [[]]
    if not lst:
        return []
    else:
        return [lst[i:i+1] + x for i in range(len(lst)) for x in combinationsOf(k-1, lst[i+1:])]

def player():
    ps = ["".join(p) for p in permutations(combinationsOf(4, [str(i) for i in range(1, 10)]))]
    play(ps)

def play(ps):
    if not ps:
        print("Unable to find a solution")
    else:
        i = randint(0, len(ps) - 1)
        p = ps[i]
        print("My guess is " + p)
        print("How many bulls and cows?")
        user_input = takeInput()
        bc = [int(c) for c in user_input]
        ps_prime = filter_ps(ps, p, bc)
        if len(ps_prime) == 1:
            print("The answer is " + ps_prime[0])
        else:
            play(ps_prime)

def takeInput():
    user_input = input()
    ui = [int(c) for c in user_input if c.isdigit()]
    if sum(ui) > 4 or len(ui) != 2:
        print("Wrong input. Try again")
        return takeInput()
    else:
        return ui