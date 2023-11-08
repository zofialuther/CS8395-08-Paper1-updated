import Data.Monoid

def main() -> None:
    xs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(str(Sum(x) for x in xs) <> mempty)
    print(str(Product(x) for x in xs) <> mempty)
    print(str([str(x) for x in xs] <> mempty))
    print(str([str(x) for x in "Love is one damned thing after each other"] <> mempty))