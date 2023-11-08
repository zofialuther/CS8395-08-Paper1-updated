from typing import List
from itertools import groupby
from operator import itemgetter
import re

def range_expand(L: str) -> List[str]:
    L = '-6,-3--1,3-5,7-11,14,15,17-20'
    print(L)
    LA = list(L)
    R = extract_Range(LA)
    LR = list(map(study_Range, R))
    LX = pack_Range(LR)
    print(LX)

def extract_Range(X: List[str]) -> List[str]:
    if not X:
        return []
    else:
        Range, X1 = get_Range(X)
        return [Range] + extract_Range(X1)

def get_Range(X: List[str]) -> (str, List[str]):
    if not X:
        return '', []
    elif X[0] == ',':
        return '', X[1:]
    else:
        EC, NEC = append_dl(X, [])
        Range, R = get_Range(NEC)
        return EC, Range, R

def append_dl(X: List[str], Y: List[str]) -> (List[str], List[str]):
    return X + Y, Y

def study_Range(Range: str) -> (int, int):
    if re.match(r'^-?\d+$', Range):
        return int(Range), int(Range)
    else:
        Deb, Fin = map(int, Range.split('-'))
        return Deb, Fin

def pack_Range(R: List[List[int]]) -> List[List[int]]:
    if not R:
        return []
    else:
        X, Rest = R[0], R[1:]
        V = [X]
        Packed = run(X, Rest, V)
        return [V] + pack_Range(Packed)

def run(Fin: int, Rest: List[List[int]], V: List[int]) -> List[List[int]]:
    if Rest:
        Other = Rest[0]
        if Fin != Deb and Fin != Deb + 1 and Other != Fin + 1:
            return [Other] + Rest
        else:
            return [Deb, Fin] + Rest
    else:
        return []

range_expand('-6,-3--1,3-5,7-11,14,15,17-20')