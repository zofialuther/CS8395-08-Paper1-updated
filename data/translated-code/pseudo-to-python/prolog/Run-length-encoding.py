from typing import List

def run_length() -> None:
    L = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"
    print(f'encode {L}')
    R = encode(L)
    print(R)
    print('decode', R)
    L1 = decode(R)
    print(L1)

def encode(In: str) -> str:
    I = list(In)
    R1 = packList(I)
    R2 = dcg_packList2List(R1, [])
    return ''.join(R2)

def dcg_packList2List(lst: List[List[str]], result: List[str]) -> List[str]:
    if lst:
        N, V = lst[0]
        result.append(str(N))
        result.append(V)
        return dcg_packList2List(lst[1:], result)
    else:
        return result

def decode(In: str) -> str:
    I = list(In)
    R1 = dcg_List2packList(I, [])
    L1 = packList(R1)
    return ''.join(L1)

def dcg_List2packList(lst: List[str], result: List[str]) -> List[str]:
    if lst:
        H = lst[0]
        if H.isdigit():
            N = parse_number(lst, 0)
            result.append(str(N))
        else:
            result.append(H)
        return dcg_List2packList(lst[1:], result)
    else:
        return result

def parse_number(lst: List[str], N: int) -> int:
    H = lst[0]
    if H.isdigit():
        N1 = N * 10 + int(H) - 48
        return parse_number(lst[1:], N1)
    else:
        return int(H)

def packList(lst: List[str]) -> List[List[str]]:
    if not lst:
        return []
    elif len(lst) == 1:
        return [[1, lst[0]]]
    else:
        X = lst[0]
        rest = lst[1:]
        XRun, RRest = run(X, rest, [], [])
        return [[1, X]] + packList(RRest)

def run(Var: str, lst: List[str], XRun: List[str], RRest: List[str]) -> List[str]:
    if not lst:
        XRun.extend([1, Var])
        return XRun, RRest
    else:
        if Var == lst[0]:
            N = 1
            while N < len(lst) and Var == lst[N]:
                N += 1
            XRun.extend([N, Var])
            return XRun, lst[N:]
        else:
            XRun.extend([1, Var])
            return XRun, lst

run_length()