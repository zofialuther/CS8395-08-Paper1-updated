from typing import List, Tuple, Union

def inconsistentChar(xs: List) -> Union[None, Tuple[int, any]]:
    if not xs:
        return None
    else:
        index = next((i for i, v in enumerate(xs) if v != xs[0]), None)
        if index is not None:
            return (index, xs[index])
        else:
            return None