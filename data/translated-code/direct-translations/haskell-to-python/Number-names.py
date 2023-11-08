from typing import List

def spell_integer(n: int) -> str:
    if n < 0:
        return "negative " + spell_integer(-n)
    elif n < 20:
        return small(n)
    elif n < 100:
        a, b = divmod(n, 10)
        return tens(a) + nonzero('-', b)
    elif n < 1000:
        a, b = divmod(n, 100)
        return small(a) + " hundred" + nonzero(' ', b)
    else:
        result = []
        for i, num in filter(lambda x: x[1] != 0, zip(range(len(str(n))), uff(n))):
            result.append(big(i, num))
        return ", ".join(result)

def nonzero(c: str, n: int) -> str:
    if n == 0:
        return ""
    else:
        return c + spell_integer(n)

def uff(n: int) -> List[int]:
    result = []
    while n > 0:
        result.append(n % 1000)
        n //= 1000
    return result

def small(n: int) -> str:
    return ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"][n]

def tens(n: int) -> str:
    return [None, None, "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"][n]

def big(e: int, n: int) -> str:
    if e == 0:
        return spell_integer(n)
    elif e == 1:
        return spell_integer(n) + " thousand"
    else:
        l = [None, None, "m", "b", "tr", "quadr", "quint", "sext", "sept", "oct", "non", "dec"]
        return spell_integer(n) + ' ' + l[e] + "illion"