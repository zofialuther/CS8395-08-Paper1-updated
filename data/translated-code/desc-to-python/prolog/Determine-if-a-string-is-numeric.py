def numeric_string(input_string):
    try:
        atom = str(input_string)
        number = float(atom)
        return True
    except ValueError:
        return False