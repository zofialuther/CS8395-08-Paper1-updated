def pangram(L):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    for c in alphabet:
        if c not in L:
            return False
    return True

def pangram_example():
    L1 = "the quick brown fox jumps over the lazy dog"
    if pangram(L1):
        R1 = "ok"
    else:
        R1 = "ko"
    print(f'{L1} --> {R1}')

    L2 = "the quick brown fox jumped over the lazy dog"
    if pangram(L2):
        R2 = "ok"
    else:
        R2 = "ko"
    print(f'{L2} --> {R2}')