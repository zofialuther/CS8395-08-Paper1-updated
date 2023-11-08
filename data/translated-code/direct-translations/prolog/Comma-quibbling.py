def test():
    print([])            # => {}
    print(["ABC"])       # => {"ABC"}
    print(["ABC", "DEF"])    # => {"ABC and DEF"}
    print(["ABC", "DEF", "G", "H"])    # => {"ABC, DEF, G and H"}
    print(True)