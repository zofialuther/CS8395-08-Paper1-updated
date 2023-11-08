def pali(input_str):
    reversed_str = input_str[::-1]
    if input_str == reversed_str:
        return True
    else:
        return False