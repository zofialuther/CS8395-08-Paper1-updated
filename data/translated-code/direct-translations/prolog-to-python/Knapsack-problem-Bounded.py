from constraint import *

# tuples (name, weights, value, nb pieces).
def knapsack():
    L = [("map", 9, 150, 1),
         ("compass", 13, 35, 1),
         ("water", 153, 200, 2),
         ("sandwich", 50, 60, 2),
         ("glucose", 15, 60, 2),
         ("tin", 68, 45, 3),
         ("banana", 27, 60, 3),
         ("apple", 39, 40, 3),
         ("cheese", 23, 30, 1),
         ("beer", 52, 10, 3),
         ("suntan cream", 11, 70, 1),
         ("camera", 32, 30, 1),
         ("T-shirt", 24, 15, 2),
         ("trousers", 48, 10, 2),
         ("umbrella", 73, 40, 1),
         ("waterproof trousers", 42, 70, 1),
         ("waterproof overclothes", 43, 75, 1),
         ("note-case", 22, 80, 1),
         ("sunglasses", 7, 20, 1),
         ("towel", 18, 12, 2),
         ("socks", 4, 50, 1),
         ("book", 30, 10, 2)]

    problem = Problem()
    Takes = [problem.createVariable("Take"+str(i), [0, item[3]]) for i, item in enumerate(L)]
    Ws = [item[1] for item in L]
    Vs = [item[2] for item in L]

    problem.addConstraint(400, "<=", Sum([W * Takes[i] for i, W in enumerate(Ws)]))
    problem.addConstraint(Sum([V * Takes[i] for i, V in enumerate(Vs)]) == VM)

    problem.getSolution()

    WM = Sum([W * Takes[i] for i, W in enumerate(Ws)])

    # displaying the results
    max_len_word = max([len(item[0]) for item in L])
    print(" " * max_len_word, end="\t")
    print(" " * 4, end="\t")
    print(" " * 5)
    for i, item in enumerate(L):
        if Takes[i].getValue() == 0:
            continue
        print(f"{Takes[i].getValue()} {item[0]}\t{item[1]}\t{item[2]}")

knapsack()