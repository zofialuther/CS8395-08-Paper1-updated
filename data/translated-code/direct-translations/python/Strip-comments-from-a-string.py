from itertools import takewhile

def stripComments(cs):
    def go(cs):
        return lambda s: ''.join(
            takewhile(lambda c: c not in cs, s)
        ).strip()
    return lambda txt: '\n'.join(map(
        go(cs),
        txt.splitlines()
    ))

if __name__ == '__main__':
    print(
        stripComments(';#')(
            '''apples, pears # and bananas
               apples, pears ; and bananas
            '''
        )
    )