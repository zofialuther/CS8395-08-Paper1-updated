def main():
    arr = [8, 9, 1, 3, 4, 2, 6, 5, 4]
    bubble_sort(arr, None)
    return

def bubble_sort(Xs, Res):
    print(Xs)
    print('\n')
    Ys, Changed = bubble_pass(Xs, Res)
    if Changed:
        bubble_sort(Ys, Res)
    else:
        Res = Xs

def bubble_pass(Xs, Res):
    X = Xs[0]
    Y = Xs[1]
    Zs = Xs[2:]
    if X > Y:
        H = Y
        T = [X] + Zs
        Changed = True
    else:
        H = X
        T = [Y] + Zs
        Changed = False
    Res = [H] + bubble_pass(T, Res)
    return Res, Changed

def test(arr):
    arr = [8, 9, 1, 3, 4, 2, 6, 5, 4]