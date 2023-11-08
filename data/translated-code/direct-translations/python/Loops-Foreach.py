d = {"fortytwo": 42, 3.14159: "pi", 23: "twentythree", "zero": 0, 13: "thirteen"}
for k in sorted(d):
    print("{}: {}".format(k, d[k]))