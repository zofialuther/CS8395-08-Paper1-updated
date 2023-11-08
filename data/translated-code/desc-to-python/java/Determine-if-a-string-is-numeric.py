def is_numeric(input_string):
    try:
        float(input_string)
        return True
    except ValueError:
        return False