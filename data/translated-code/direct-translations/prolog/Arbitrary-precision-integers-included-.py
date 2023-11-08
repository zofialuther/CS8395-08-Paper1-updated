def task(Length):
    N = 5 ** 4 ** 3 ** 2
    Codes = list(str(N))
    prefix = list("62060698786608744707")
    suffix = list("92256259918212890625")

    if Codes[:len(prefix)] == prefix and Codes[-len(suffix):] == suffix:
        Length = len(Codes)