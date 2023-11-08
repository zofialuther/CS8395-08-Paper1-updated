cats1 = [div(product(enumFromTo(2 + x)(2 * x)))(product(enumFromTo 1 x)) | x <- [0..]]

cats2 = 1 : [sum(zipWith(*) (reverse(take n cats2)) cats2) | n <- [1..]]

cats3 = scanl(\c n -> c * 2 * (2 * n - 1) `div` (succ n)) 1 [1..]

def main():
    for cat_list in [cats1, cats2, cats3]:
        print([x for x in cat_list][:15])

main()