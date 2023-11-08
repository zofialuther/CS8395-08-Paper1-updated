```python
class MertensFunction:

    MU_MAX = 100000000
    MU = None
    MERTEN = None

    # Compute mobius and merten function via sieve
    @staticmethod
    def merten_function(n):
        if MertensFunction.MERTEN is not None:
            return MertensFunction.MERTEN[n]

        MertensFunction.MU = [1] * (MertensFunction.MU_MAX + 1)
        MertensFunction.MERTEN = [0] * (MertensFunction.MU_MAX + 1)
        MertensFunction.MERTEN[1] = 1
        sqrt = int(MertensFunction.MU_MAX ** 0.5)
        for i in range(sqrt):
            MertensFunction.MU[i] = 1

        for i in range(2, sqrt + 1):
            if MertensFunction.MU[i] == 1:
                for j in range(i, MertensFunction.MU_MAX + 1, i):
                    MertensFunction.MU[j] *= -i
                for j in range(i * i, MertensFunction.MU_MAX + 1, i * i):
                    MertensFunction.MU[j] = 0

        sum = 1
        for i in range(2, MertensFunction.MU_MAX + 1):
            if MertensFunction.MU[i] == i:
                MertensFunction.MU[i] = 1
            elif MertensFunction.MU[i] == -i:
                MertensFunction.MU[i] = -1
            elif MertensFunction.MU[i] < 0:
                MertensFunction.MU[i] = 1
            elif MertensFunction.MU[i] > 0:
                MertensFunction.MU[i] = -1
            sum += MertensFunction.MU[i]
            MertensFunction.MERTEN[i] = sum
        return MertensFunction.MERTEN[n]

    @staticmethod
    def main():
        print("First 199 terms of the merten function are as follows:\n    ")
        for n in range(1, 200):
            print("{:2d}  ".format(MertensFunction.merten_function(n)), end="")
            if (n + 1) % 20 == 0:
                print("\n")

        for exponent in range(3, 9):
            zero_count = 0
            zero_crossing_count = 0
            positive_count = 0
            negative_count = 0
            m_sum = 0
            m_min = float('inf')
            m_min_index = 0
            m_max = float('-inf')
            m_max_index = 0
            n_max = 10 ** exponent
            for n in range(1, n_max + 1):
                m = MertensFunction.merten_function(n)
                m_sum += m
                if m < m_min:
                    m_min = m
                    m_min_index = n
                if m > m_max:
                    m_max = m
                    m_max_index = n
                if m > 0:
                    positive_count += 1
                if m < 0:
                    negative_count += 1
                if m == 0:
                    zero_count += 1
                if m == 0 and MertensFunction.merten_function(n - 1) != 0:
                    zero_crossing_count += 1
            print("\nFor M(x) with x from 1 to {:,d}".format(n_max))
            print("The maximum of M(x) is M({:,d}) = {:,d}.".format(m_max_index, m_max))
            print("The minimum of M(x) is M({:,d}) = {:,d}.".format(m_min_index, m_min))
            print("The sum of M(x) is {:,d}.".format(m_sum))
            print("The count of positive M(x) is {:,d}, count of negative M(x) is {:,d}.".format(positive_count, negative_count))
            print("M(x) has {:,d} zeroes in the interval.".format(zero_count))
            print("M(x) has {:,d} crossings in the interval.".format(zero_crossing_count))


MertensFunction.main()
```