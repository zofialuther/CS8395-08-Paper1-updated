import java.math.BigInteger
import java.util.HashMap
import java.util.Map

class SterlingNumbersFirstKind:

    def main(args):
        print("Unsigned Stirling numbers of the first kind:")
        max = 12
        print("n/k", end="")
        for n in range(max+1):
            print(f"{n:10}", end="")
        print()
        for n in range(max+1):
            print(f"{n:<3}", end="")
            for k in range(n+1):
                print(f"{sterling1(n, k):10s}", end="")
            print()
        print("The maximum value of S1(100, k) = ")
        previous = BigInteger.ZERO
        for k in range(1, 101):
            current = sterling1(100, k)
            if current.compareTo(previous) > 0:
                previous = current
            else:
                print(f"{previous}\n({len(previous.toString())} digits, k = {k-1})")
                break

    COMPUTED = HashMap()

    def sterling1(n, k):
        key = f"{n},{k}"
        if key in COMPUTED:
            return COMPUTED.get(key)
        if n == 0 and k == 0:
            return BigInteger.valueOf(1)
        if n > 0 and k == 0:
            return BigInteger.ZERO
        if k > n:
            return BigInteger.ZERO
        result = sterling1(n-1, k-1).add(BigInteger.valueOf(n-1).multiply(sterling1(n-1, k)))
        COMPUTED.put(key, result)
        return result