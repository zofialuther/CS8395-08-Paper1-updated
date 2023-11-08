from typing import List
import bisect

class GuessNumber:
    LOWER = 0
    UPPER = 100

    @staticmethod
    def main(args: List[str]) -> None:
        print("Instructions for the game")

        class NumberList(list):
            def size(self):
                return GuessNumber.UPPER - GuessNumber.LOWER

            def __getitem__(self, index):
                guess = int(input(f"Is your number {index}? (-1 for lower, 1 for higher, 0 for correct): "))
                if guess == -1:
                    return -1
                elif guess == 1:
                    return 1
                else:
                    return 0

        nums = NumberList(range(GuessNumber.LOWER, GuessNumber.UPPER))
        result = bisect.bisect_left(nums, 50)
        if result < 0:
            print("That is impossible.")
        else:
            print(f"Your number is {nums[result]}")