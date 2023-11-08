from typing import List, Tuple
from text import printf

input: List[Tuple[str, str]] = [ ("", ' ')
        , ("The better the 4-wheel drive, the further you'll be from help when ya get stuck!", 'e')
        , ("headmistressship", 's')
        , ("\"If I were two-faced, would I be wearing this one?\" --- Abraham Lincoln ", '-')
        , ("..1111111111111111111111111111111111111111111111111111111111111117777888", '7')
        , ("I never give 'em hell, I just tell the truth, and they think it's hell. ", '.')
        , ("                                                    --- Harry S Truman  ", 'r')
        , ("aardvark", 'a')
        , ("😍😀🙌💃😍😍😍🙌", '😍')
        ]

def collapse(s: List[str], c: str) -> List[str]:
    def go(s):
        if len(s) == 0:
            return []
        elif len(s) == 1:
            return s
        else:
            x, y, *xs = s
            if x == y and x == c:
                return go([y, *xs])
            else:
                return [x, *go([y, *xs])]
    return go(s)

def main():
    for a, b in map(lambda x: (x[0], collapse(x[0], x[1])), input):
        printf("squeeze: '%c'\nold: %3d «««%s»»»\nnew: %3d «««%s»»»\n\n" % (c, len(a), a, len(b), b))

main()