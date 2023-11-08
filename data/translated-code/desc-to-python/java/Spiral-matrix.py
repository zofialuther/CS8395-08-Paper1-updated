class Blah:
    def main(self):
        array = self.getSpiralArray(5)
        self.print2dArray(array)
    
    def getSpiralArray(self, n):
        result = [[0]*n for _ in range(n)]
        top, bottom, left, right = 0, n-1, 0, n-1
        num = 1
        
        while top <= bottom and left <= right:
            for i in range(left, right+1):
                result[top][i] = num
                num += 1
            top += 1
            
            for i in range(top, bottom+1):
                result[i][right] = num
                num += 1
            right -= 1
            
            for i in range(right, left-1, -1):
                result[bottom][i] = num
                num += 1
            bottom -= 1
            
            for i in range(bottom, top-1, -1):
                result[i][left] = num
                num += 1
            left += 1
        
        return result
    
    def print2dArray(self, array):
        for row in array:
            for elem in row:
                print(elem, end=' ')
            print()