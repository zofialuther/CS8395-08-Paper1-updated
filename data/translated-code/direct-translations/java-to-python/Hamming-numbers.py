from queue import PriorityQueue
from math import pow

class Hamming:
    THREE = 3
    FIVE = 5

    @staticmethod
    def updateFrontier(x, pq):
        pq.put(x << 1)
        pq.put(x * Hamming.THREE)
        pq.put(x * Hamming.FIVE)

    @staticmethod
    def hamming(n):
        if n <= 0:
            raise ValueError("Invalid parameter")
        frontier = PriorityQueue()
        Hamming.updateFrontier(1, frontier)
        lowest = 1
        for i in range(1, n):
            lowest = frontier.get()
            while not frontier.empty() and frontier.queue[0] == lowest:
                frontier.get()
            Hamming.updateFrontier(lowest, frontier)
        return lowest

    @staticmethod
    def main():
        print("Hamming(1 .. 20) =", end="")
        for i in range(1, 21):
            print(" " + str(Hamming.hamming(i)), end="")
        print("\nHamming(1691) = " + str(Hamming.hamming(1691)))
        print("Hamming(1000000) = " + str(Hamming.hamming(1000000)))

if __name__ == "__main__":
    Hamming.main()