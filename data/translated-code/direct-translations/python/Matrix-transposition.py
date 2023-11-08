def transpose(m):
    if m:
        inner = type(m[0])
        z = zip(*m)
        return (type(m))(
            list(map(inner, z)) if isinstance(inner, tuple) else z
        )
    else:
        return m


if __name__ == '__main__':
    tts = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    tls = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    emptyTuple = ()
    lls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lts = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    emptyList = []

    print('transpose function :: (Transposition without type change):\n')
    for m in [emptyTuple, tts, tls, emptyList, lls, lts]:
        tm = transpose(m)
        print(
            type(tm).__name__ + (
                (' of ' + type(tm[0]).__name__) if m else ''
            ) + ' :: ' + str(m) + ' -> ' + str(tm)
        )