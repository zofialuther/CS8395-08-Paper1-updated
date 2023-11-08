def commentstripper(input_string):
    # function to remove comments from input string
    # code to remove comments
    return result_string

def test():
    # non-nested block comment example
    print('''
    /* This is a non-nested block comment example */
    This is some code with // a line comment
    var x = 5; // this is a comment after code
    ''')
    print(commentstripper('''
    /* This is a non-nested block comment example */
    This is some code with // a line comment
    var x = 5; // this is a comment after code
    '''))

    # nested block comment example
    print('''
    /* This is a
    nested block comment example */
    This is some code with /*
    a nested comment
    */
    var y = 10; /* this is a comment after code */
    ''')
    print(commentstripper('''
    /* This is a
    nested block comment example */
    This is some code with /*
    a nested comment
    */
    var y = 10; /* this is a comment after code */
    '''))

if __name__ == "__main__":
    test()