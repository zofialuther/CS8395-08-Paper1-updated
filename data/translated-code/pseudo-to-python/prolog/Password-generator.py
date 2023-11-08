from random import shuffle, choice

def main(Argv):
    Spec = [
        ['help', 'boolean', False, ['h'], ['help'], 'Show Help'],
        ['length', 'integer', 10, ['l'], ['length'], 'Specify the length of each password.'],
        ['number', 'integer', 1, ['n'], ['number'], 'Specify the number of passwords to create.']
    ]

    Opts = opt_parse(Spec, Argv)
    if {'help': True} in Opts:
        show_help(Spec)
    else:
        Len = next(item for item in Opts if item[0] == 'length')[1]
        Num = next(item for item in Opts if item[0] == 'number')[1]
        print_set_of_passwords(Len, Num)

def show_help(Spec):
    HelpText = opt_help(Spec)
    print('Usage: swipl pgen.pl <options>\n\n')
    print(HelpText)

def print_set_of_passwords(Length, Number):
    for _ in range(Number):
        pword = random_pword(Length)
        print(''.join(pword))

def random_pword(Length):
    GenPword = [''] * Length
    PwordChars = [c for c in "!\"#$%&'()*+,-./:;<=>?@[]^_{|}~"] + [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
    
    while True:
        for i in range(Length):
            GenPword[i] = populate_pword(PwordChars)
        if all(pword_char_rule(GenPword, t) for t in ['lower', 'upper', 'digits', 'special']):
            shuffle(GenPword)
            return GenPword

def populate_pword(PwordChars):
    return choice(PwordChars)

def pword_char_rule(Pword, Type):
    return pword_char(Type) in Pword

def pword_char(Type):
    if Type == 'lower':
        return [c for c in "abcdefghijklmnopqrstuvwxyz"]
    elif Type == 'upper':
        return [c for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    elif Type == 'digits':
        return [str(i) for i in range(10)]
    elif Type == 'special':
        return [c for c in "!\"#$%&'()*+,-./:;<=>?@[]^_{|}~"]