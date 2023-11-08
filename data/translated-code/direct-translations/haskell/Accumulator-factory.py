from Control.Monad.ST import ST, runST
from Data.STRef import STRef, newSTRef, readSTRef, modifySTRef

def accumulator(sum0):
    def inner(n):
        modifySTRef(sum, lambda x: x + n)
        return readSTRef(sum)
    
    sum = newSTRef(sum0)
    return inner

def main():
    foo = runST(lambda: 
                x = accumulator(1)
                x(5)
                accumulator(3)
                x(2.3)
            )
    print(foo)

main()