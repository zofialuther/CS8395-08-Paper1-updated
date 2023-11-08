from Control.Lens
import Data.Numbers.Primes
import Text.Printf

data Group a = Group { _count :: Int, _results :: [a] }
type Groups = ( Group (Int, Int), Group (Int, Int, Int), Group (Int, Int, Int, Int), Group (Int, Int, Int, Int, Int), Group Int )

initialGroups = let newGroup = Group 0 [] in (newGroup, newGroup, newGroup, newGroup, newGroup)

collect r@(pr, tt, qd, qn, un) n
  | isPrime n4 && isPrime n3 && isPrime n2 && isPrime n1 = (addPair pr, addTriplet tt, addQuad qd, addQuin qn, un)
  | isPrime n3 && isPrime n2 && isPrime n1               = (addPair pr, addTriplet tt, addQuad qd, qn, un)
  | isPrime n2 && isPrime n1                             = (addPair pr, addTriplet tt, qd, qn, un)
  | isPrime n1                                           = (addPair pr, tt, qd, qn, un)
  | not (isPrime (n+6)) && not (isPrime n1)              = (pr, tt, qd, qn, addUnSexy un)
  | otherwise                                            = r
  where
    n1 = n-6
    n2 = n-12
    n3 = n-18
    n4 = n-24

    addPair    = over count succ . over results (take 5  . (:) (n1, n))
    addTriplet = over count succ . over results (take 5  . (:) (n2, n1, n))
    addQuad    = over count succ . over results (take 5  . (:) (n3, n2, n1, n))
    addQuin    = over count succ . over results (take 1  . (:) (n4, n3, n2, n1, n))
    addUnSexy  = over count succ . over results (take 10 . (:) n)

def display(lst):
    return str(list(reversed(lst)))

def main():
    pr, tt, qd, qn, un = collectGroups(primes)
    print(f"Number of sexy prime pairs: {pr._count}\n  Last 5 : {display(pr._results)}\n")
    print(f"Number of sexy prime triplets: {tt._count}\n  Last 5 : {display(tt._results)}\n")
    print(f"Number of sexy prime quadruplets: {qd._count}\n  Last 5 : {display(qd._results)}\n")
    print(f"Number of sexy prime quintuplets: {qn._count}\n  Last 1 : {display(qn._results)}\n")
    print(f"Number of unsexy primes: {un._count}\n  Last 10: {display(un._results)}\n")
    collectGroups = foldl(collect, initialGroups, list(takewhile(lambda x: x < 1000035, primes)))

main()