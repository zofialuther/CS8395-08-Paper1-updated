import queue

class Hamming:
    THREE = 3
    FIVE = 5

    def updateFrontier(self, x, pq):
        pq.put(x << 1)
        pq.put(x * self.THREE)
        pq.put(x * self.FIVE)

    def hamming(self, n):
        if n <= 0:
            raise ValueError("Invalid parameter")
        frontier = queue.PriorityQueue()
        self.updateFrontier(1, frontier)
        lowest = 1
        for i in range(1, n):
            lowest = frontier.get()
            while frontier and frontier.queue[0] == lowest:
                frontier.get()
            self.updateFrontier(lowest, frontier)
        return lowest

    def main(self):
        print("Hamming(1 .. 20) =")
        for i in range(1, 21):
            print(" " + str(self.hamming(i)), end="")
        print("\nHamming(1691) = " + str(self.hamming(1691)))
        print("Hamming(1000000) = " + str(self.hamming(1000000)))



hamming = Hamming()
hamming.main()