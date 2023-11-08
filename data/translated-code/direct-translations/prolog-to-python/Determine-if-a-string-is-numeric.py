def numeric_string(string):
    try:
        atom = str(string)
        _ = int(atom)
        return True
    except ValueError:
        return False