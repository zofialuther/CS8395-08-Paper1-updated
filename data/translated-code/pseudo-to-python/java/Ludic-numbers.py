class Ludic:
    def ludicUpTo(self, n):
        ludics = []
        for i in range(1, n+1):
            ludics.append(i)
        
        cursor = 1
        while cursor < len(ludics):
            removeCursor = cursor + ludics[cursor]
            while removeCursor < len(ludics):
                ludics.pop(removeCursor)
                removeCursor += ludics[cursor] - 1
            cursor += 1
        
        return ludics
    
    def getTriplets(self, ludics):
        triplets = []
        for i in range(len(ludics)):
            if ludics[i] + 2 in ludics and ludics[i] + 6 in ludics:
                triplet = [ludics[i], ludics[i] + 2, ludics[i] + 6]
                triplets.append(triplet)
        
        return triplets

    def main(self):
        ludic = Ludic()
        print(ludic.ludicUpTo(110))
        print(len(ludic.ludicUpTo(1000)))
        subList = ludic.ludicUpTo(22000)[1999:2005]
        print(subList)
        print(ludic.getTriplets(ludic.ludicUpTo(250)))