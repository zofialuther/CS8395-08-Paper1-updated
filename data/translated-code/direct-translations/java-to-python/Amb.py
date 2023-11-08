from typing import List, Tuple
from functools import reduce

def main() -> None:
    words: List[List[str]] = [
        ["the", "that", "a"],
        ["frog", "elephant", "thing"],
        ["walked", "treaded", "grows"],
        ["slowly", "quickly"]
    ]
    print(amb(words))

def amb(a_options: List[List[str]]) -> str:
    def continues(before: str, after: str) -> bool:
        return before.endswith(after[0])

    amb_result: List[str] = amb_helper(continues, a_options, "")
    return "No match found" if not amb_result else " ".join(amb_result)

def amb_helper(a_bi_function, a_options: List[List[str]], a_previous: str) -> List[str]:
    if not a_options:
        return []

    for option in a_options[0]:
        if a_previous and not a_bi_function(a_previous, option):
            continue

        if len(a_options) == 1:
            return [option]

        result: List[str] = amb_helper(a_bi_function, a_options[1:], option)

        if result:
            result.insert(0, option)
            return result

    return []

if __name__ == "__main__":
    main()