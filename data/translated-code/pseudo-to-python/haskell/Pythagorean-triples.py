def pytr(n):
    filtered_triples = list(filter(
        lambda tpl: tpl[1] + tpl[2] + tpl[3] <= n,
        [
            (prim(a, b, c), a, b, c)
            for a in xs
            for b in drop(a, xs)
            for c in drop(b, xs)
            if a ** 2 + b ** 2 == c ** 2
        ]
    ))
    return filtered_triples

def main():
    xs = pytr(100)
    num_triples = len(xs)
    num_primitive_triples = len(list(filter(lambda tpl: tpl[0], xs))
    print("Up to 100 there are " + str(num_triples) + " triples, of which " + str(num_primitive_triples) + " are primitive.")

xs = pytr(100)