def fractran_primes():
    i = 1
    while True:
        fr = fractran(2)[i]
        binstr = bin(fr)[2:]
        if binstr.count('1') == 1:
            prime = binstr.count('0')
            if prime > 1:
                yield prime, i
        i += 1

if __name__ == 'main':
    for i in range(1, 16):
        prime, index = next(fractran_primes())
        print("Generated prime %2i from the %6i'th member of the fractran series" % (prime, index))