from typing import List
import operator

wds: List[str] = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]

def main() -> None:
    print(max(wds, key=len))