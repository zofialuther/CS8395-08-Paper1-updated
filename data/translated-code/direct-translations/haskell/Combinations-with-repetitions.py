def combinationsWithRepetition(k, xs):
    def cmb(n, peers):
        if n == 0:
            return peers
        if not peers:
            return cmb(n - 1, [[x] for x in xs])
        else:
            return cmb(n - 1, [p + [x] for p in peers for x in xs])

    return cmb(k, [])

print(combinationsWithRepetition(2, ["iced", "jam", "plain"]))
print(len(combinationsWithRepetition(3, list(range(10))))