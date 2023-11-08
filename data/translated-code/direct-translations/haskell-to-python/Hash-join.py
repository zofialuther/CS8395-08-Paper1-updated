```python
import Data.HashTable.ST.Basic as H
import Data.Hashable
import Control.Monad.ST
import Control.Monad
import Data.STRef

def hashJoin(xs, fx, ys, fy):
    def runST():
        l = newSTRef([])
        ht = H.new
        for y in ys:
            H.insert(ht, fy(y), (H.lookup(ht, fy(y)) if H.lookup(ht, fy(y)) is not None else [y]))
        for x in xs:
            if H.lookup(ht, fx(x)) is not None:
                modifySTRef(l, (map((x, v) for v in H.lookup(ht, fx(x))) + ))
        return readSTRef(l)

mapM_(print, hashJoin([(1, "Jonah"), (2, "Alan"), (3, "Glory"), (4, "Popeye")], snd, [("Jonah", "Whales"), ("Jonah", "Spiders"), ("Alan", "Ghosts"), ("Alan", "Zombies"), ("Glory", "Buffy")], fst))
```