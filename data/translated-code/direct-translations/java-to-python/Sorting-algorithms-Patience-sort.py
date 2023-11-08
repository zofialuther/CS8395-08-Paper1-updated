from queue import PriorityQueue
from typing import TypeVar, List, Generic

E = TypeVar('E', bound=Comparable)


class PatienceSort:
    @staticmethod
    def sort(n: List[E]) -> None:
        piles: List[Pile[E]] = []
        # sort into piles
        for x in n:
            new_pile = Pile()
            new_pile.push(x)
            i = bisect_left(piles, new_pile)
            if i < 0:
                i = ~i
            if i != len(piles):
                piles[i].push(x)
            else:
                piles.append(new_pile)

        # priority queue allows us to retrieve least pile efficiently
        heap = PriorityQueue(piles)
        for c in range(len(n)):
            small_pile = heap.get()
            n[c] = small_pile.pop()
            if not small_pile.is_empty():
                heap.put(small_pile)
        assert heap.empty()

    @staticmethod
    def main() -> None:
        a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
        sort(a)
        print(a)
        

class Pile(Generic[E], Stack[E], Comparable[Pile[E]]):
    def compare_to(self, y: Pile[E]) -> int:
        return self.peek().compare_to(y.peek())


PatienceSort.main()