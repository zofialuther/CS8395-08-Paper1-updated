from typing import List, Tuple, Union

def inconsistentChar(elements: List) -> Union[None, Tuple[int, str]]:
    if not elements:
        return None
    else:
        first_element = elements[0]
        index = next((i for i, v in enumerate(elements) if v != first_element), None)
        if index is not None:
            return (index, elements[index])
        else:
            return None