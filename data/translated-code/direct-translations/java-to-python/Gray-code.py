from math import pow

class GrayCode:
    @staticmethod
    def gray_encode(n):
        return n ^ (n >> 1)

    @staticmethod
    def gray_decode(n):
        p = n
        while (n := n >> 1) != 0:
            p ^= n
        return p

    @staticmethod
    def gray_encode_biginteger(n):
        return n ^ (n >> 1)

    @staticmethod
    def gray_decode_biginteger(n):
        p = n
        while (n := n >> 1).signum() != 0:
            p = p ^ n
        return p

    @staticmethod
    def gray_decode2_biginteger(n):
        n_bits = bin(int(n))[2:]
        result = n_bits[0]
        for i in range(1, len(n_bits)):
            result += "1" if n_bits[i] != result[i - 1] else "0"
        return int(result, 2)

    @staticmethod
    def gray_encode2(n):
        result = 0
        exp = 0
        while n > 0:
            next_highest_bit = (n >> 1) & 1
            if next_highest_bit == 1:
                result += (1 << exp) if (n & 1) == 0 else 0
            else:
                result += (n & 1) * (1 << exp)
            n >>= 1
            exp += 1
        return result

    @staticmethod
    def main():
        print("i\tBinary\tGray\tGray2\tDecoded")
        print("=======================================")
        for i in range(32):
            print(str(i) + "\t" + bin(i)[2:] + "\t" + bin(GrayCode.gray_encode(i))[2:] + "\t" + bin(GrayCode.gray_encode2(i))[2:] + "\t" + str(GrayCode.gray_decode(GrayCode.gray_encode(i))))
        print()

        base = pow(10, 25) + 12345678901234567890
        for i in range(5):
            test = base + i
            print("test decimal      = " + str(test))
            print("gray code decimal = " + str(GrayCode.gray_encode(test)))
            print("gray code binary  = " + bin(GrayCode.gray_encode(test))[2:])
            print("decoded decimal   = " + str(GrayCode.gray_decode(GrayCode.gray_encode(test)))
            print("decoded2 decimal  = " + str(GrayCode.gray_decode2_biginteger(GrayCode.gray_encode(test)))
            print()
          
GrayCode.main()