from java.math import BigInteger

class IntegerPower:
    @staticmethod
    def main(args):
        power = BigInteger.valueOf(4).pow(3).intValueExact()
        result = BigInteger.valueOf(3).pow(2)
        power = BigInteger.valueOf(5).pow(result)
        power_str = str(power)
        length = len(power_str)
        print("5**4**3**2 = %s...%s and has %d digits%n" % (power_str[:20], power_str[-20:], length))