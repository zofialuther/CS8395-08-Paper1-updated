def pytr(n):
    xs = [i for i in range(1, n+1)]
    result = filter(lambda x: x[1] + x[2] + x[3] <= n, [(prim(a, b, c), a, b, c) for a in xs for b in xs[a-1:] for c in xs[b-1:] if a**2 + b**2 == c**2])
    return result

def main():
    xs = pytr(100)
    total_triples = len(xs)
    primitive_triples = len([x for x in xs if x[0]])
    print(f"Up to 100 there are {total_triples} triples, of which {primitive_triples} are primitive.")

main()