from dataclasses import dataclass
from typing import List
import dataclasses
import numpy as np

@dataclass
class LcmDigits:
    lcm: int

    def lcm_digits(self):
        return np.lcm.reduce(range(1, self.lcm + 1))  # 360360


@dataclass
class UpperLimit:
    all_digits: int
    lcm_digits: int

    def upper_limit(self):
        return self.all_digits - (self.all_digits % self.lcm_digits)


@dataclass
class Main:
    upper_limit: int
    lcm_digits: int

    def main(self):
        results = [self.upper_limit]
        current = self.upper_limit - self.lcm_digits
        while current >= 1:
            results.append(current)
            current -= self.lcm_digits
        return results


lcm_digits = LcmDigits(15)
lcm_result = lcm_digits.lcm_digits()

upper_limit = UpperLimit(0xfedcba987654321, lcm_result)
upper_limit_result = upper_limit.upper_limit()

main = Main(upper_limit_result, lcm_result)
main_result = main.main()
print(main_result)