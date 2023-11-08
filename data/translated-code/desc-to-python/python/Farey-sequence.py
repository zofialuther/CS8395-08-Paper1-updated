def farey_sequence(order):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    sequence = [(0, 1), (1, 1)]
    for d in range(2, order + 1):
        for n in range(1, d):
            if gcd(n, d) == 1:
                sequence.append((n, d))
    
    return sequence

def farey_length(order):
    return sum(1 for i in farey_sequence(order))

def display_farey_sequence(order):
    sequence = farey_sequence(order)
    for term in sequence:
        print("{}/{}".format(term[0], term[1]))

def test_farey_sequence():
    order = 5
    print("Farey sequence of order", order, ":")
    display_farey_sequence(order)
    print("Length of Farey sequence of order", order, "is", farey_length(order))

test_farey_sequence()