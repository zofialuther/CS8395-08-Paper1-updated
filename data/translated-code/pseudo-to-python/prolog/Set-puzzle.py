def do_it(N):
    card_sets(N, Cards, Sets)
    if card_sets(N, Cards, Sets):
        print('Cards: ')
        for Card in Cards:
            print_card(Card)
        print('Sets: ')
        for Set in Sets:
            print_set(Set)

def print_card(Card):
    print('  ' + Card[0] + ' ' + Card[1] + ' ' + Card[2] + ' ' + Card[3])

def print_set(Set):
    for Card in Set:
        print_card(Card)
    print('\n')

def n_9_4():
    return

def n_12_6():
    return

def card_sets(N, Cards, Sets):
    n(N, L)
    while True:
        random_deal(N, Cards)
        set = setof(Set, is_card_set(Cards, Set))
        if len(Sets) == L:
            return True

def random_card(Card):
    C = random.choice(['red', 'green', 'purple'])
    S = random.choice(['oval', 'squiggle', 'diamond'])
    N = random.choice(['one', 'two', 'three'])
    Sh = random.choice(['solid', 'open', 'striped'])
    Card = [C, S, N, Sh]

def random_deal(N, Cards):
    Cards = [None]*N
    for i in range(1, N+1):
        Cards[i-1] = random_card()

def is_card_set(Cards, Result):
    for i in range(len(Cards)-2):
        for j in range(i+1, len(Cards)-1):
            for k in range(j+1, len(Cards)):
                if match(Cards[i], Cards[j], Cards[k]):
                    Result = sorted([Cards[i], Cards[j], Cards[k]])

def match(T1, T2, T3):
    if T1 == T2 == T3:
        return True
    elif T1 != T2 and T2 != T3 and T1 != T3:
        return True
    else:
        return False