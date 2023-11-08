from typing import List

def extractRange(nums: List[int]) -> str:
    def f(nums: List[int]) -> List[str]:
        if len(nums) >= 3:
            x1, x2, x3, *rest = nums
            if x1 + 1 == x2 and x2 + 1 == x3:
                xn, xs_ = g(x3 + 1, rest)
                return [str(x1) + '-' + str(xn)] + f(xs_)
        if len(nums) >= 1:
            x, *rest = nums
            return [str(x)] + f(rest)
        return []

    def g(a: int, nums: List[int]) -> (int, List[int]):
        if nums and a == nums[0]:
            return g(a + 1, nums[1:])
        else:
            return a - 1, nums

    return ','.join(f(nums))