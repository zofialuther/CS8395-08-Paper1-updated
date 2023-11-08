from math import sqrt

class MersenneFactorCheck:

    TWO = 2

    @staticmethod
    def is_prime(n):
        if n == 2:
            return True
        if n < 2 or n % 2 == 0:
            return False
        max_factor = int(sqrt(n))
        for possible_factor in range(3, max_factor + 1, 2):
            if n % possible_factor == 0:
                return False
        return True

    @staticmethod
    def find_factor_mersenne_number(prime_p):
        if prime_p <= 0:
            raise ValueError("prime_p must be a positive integer")
        big_p = pow(2, prime_p) - 1
        max_factor = pow(2, (prime_p + 1) // 2)
        two_p = prime_p * 2
        possible_factor = 1
        possible_factor_bits12 = 0
        two_p_bits12 = prime_p & 3

        while possible_factor <= max_factor:
            possible_factor += two_p
            possible_factor_bits12 = (possible_factor_bits12 + two_p_bits12) & 3
            if possible_factor_bits12 == 0 or possible_factor_bits12 == 3:
                if pow(2, big_p, possible_factor) == 1:
                    return possible_factor
        return None

    @staticmethod
    def check_mersenne_number(p):
        if not MersenneFactorCheck.is_prime(p):
            print("M" + str(p) + " is not prime")
            return
        factor = MersenneFactorCheck.find_factor_mersenne_number(p)
        if factor is None:
            print("M" + str(p) + " is prime")
        else:
            print("M" + str(p) + " is not prime, has factor " + str(factor))
        return

    @staticmethod
    def main():
        for p in range(1, 51):
            MersenneFactorCheck.check_mersenne_number(p)
        MersenneFactorCheck.check_mersenne_number(929)
        return

MersenneFactorCheck.main()