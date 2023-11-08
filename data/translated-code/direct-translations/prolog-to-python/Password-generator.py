from random import sample
import string

def main(argv):
    spec = opt_spec()
    opts, _ = opt_parse(spec, argv)

    if any(opt == ('help', True) for opt in opts):
        show_help(spec)
    else:
        length = next(opt[1] for opt in opts if opt[0] == 'length')
        number = next(opt[1] for opt in opts if opt[0] == 'number')
        print_set_of_passwords(length, number)

def show_help(spec):
    helptext = opt_help(spec)
    print('Usage: swipl pgen.pl <options>\n\n' + helptext)

def opt_spec():
    return [
        ['help', 'boolean', False, ['h'], ['help'], 'Show Help'],
        ['length', 'integer', 10, ['l'], ['length'], 'Specify the length of each password.'],
        ['number', 'integer', 1, ['n'], ['number'], 'Specify the number of passwords to create.']
    ]

def opt_help(spec):
    return '\n'.join(f'-{shortflags[0]}, --{longflags[0]}\t{help}' for _, _, _, shortflags, longflags, help in spec)

def print_set_of_passwords(length, number):
    for _ in range(number):
        pword = ''.join(sample(string.ascii_letters + string.digits + string.punctuation, length))
        print(pword)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])