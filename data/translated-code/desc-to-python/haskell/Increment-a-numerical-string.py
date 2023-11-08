bool_value = bool("False")
bool_value = bool_value.__bool__()
bool_value = bool_value.__int__()
bool_value = bool_value.__index__()

result = str(bool_value)