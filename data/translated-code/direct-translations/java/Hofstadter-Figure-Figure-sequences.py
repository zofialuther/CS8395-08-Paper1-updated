from typing import List

class Hofstadter:
    @staticmethod
    def get_sequence(rlist_size: int, slist_size: int) -> List[int]:
        rlist = [1, 3, 7]
        slist = [2, 4, 5, 6]
        list_ = rlist if rlist_size > 0 else slist
        target_size = rlist_size if rlist_size > 0 else slist_size
        while len(list_) > target_size:
            list_.pop()
        while len(list_) < target_size:
            last_r = rlist[-1]
            r = last_r + slist[-1]
            rlist.append(r)
            s = last_r + 1
            while s < r and len(list_) < target_size:
                slist.append(s)
                s += 1
        return list_

    @staticmethod
    def ffr(n: int) -> int:
        return Hofstadter.get_sequence(n, 0)[n - 1]

    @staticmethod
    def ffs(n: int) -> int:
        return Hofstadter.get_sequence(0, n)[n - 1]

    @staticmethod
    def main():
        print("R():", end='')
        for n in range(1, 11):
            print(" " + str(Hofstadter.ffr(n)), end='')
        print()

        first_40_r = set()
        for n in range(1, 41):
            first_40_r.add(Hofstadter.ffr(n))

        first_960_s = set()
        for n in range(1, 961):
            first_960_s.add(Hofstadter.ffs(n))

        for i in range(1, 1001):
            if (i in first_40_r) == (i in first_960_s):
                print(f"Integer {i} either in both or neither set")
        print("Done")

Hofstadter.main()