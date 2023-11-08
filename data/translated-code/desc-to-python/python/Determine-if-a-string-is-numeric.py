def numeric(input_str):
    try:
        value = int(input_str)
    except ValueError:
        try:
            value = float(input_str)
        except ValueError:
            try:
                value = complex(input_str)
            except ValueError:
                return None
    return value

test_strings = ["123", "3.14", "5+2j", "0b1010", "0o755", "0xFF", "abc"]
for test in test_strings:
    print(f"Input: {test}")
    print(f"Numeric value: {numeric(test)}")
    print(f"isnumeric method: {test.isnumeric()}")
    print("------")