def generate_permutations(apartment_dwellers, a_set, cur_permutation):
    for s in apartment_dwellers:
        if s not in cur_permutation:
            next_permutation = cur_permutation + s
            if len(next_permutation) == len(apartment_dwellers):
                a_set.add(next_permutation)
            else:
                generate_permutations(apartment_dwellers, a_set, next_permutation)

def top_floor(permutation, person):
    return permutation.endswith(person)

def bottom_floor(permutation, person):
    return permutation.startswith(person)

def lives_above(permutation, upper_person, lower_person):
    return permutation.index(upper_person) > permutation.index(lower_person)

def adjacent(permutation, person1, person2):
    return abs(permutation.index(person1) - permutation.index(person2)) == 1

def is_possible(s):
    if top_floor(s, "B"):
        return False
    if bottom_floor(s, "C"):
        return False
    if top_floor(s, "F") or bottom_floor(s, "F"):
        return False
    if not lives_above(s, "M", "C"):
        return False
    if adjacent(s, "S", "F"):
        return False
    return not adjacent(s, "F", "C")

def main(args):
    a_set = set()
    generate_permutations(["B", "C", "F", "M", "S"], a_set, "")
    for iterator in a_set.copy():
        if not is_possible(iterator):
            a_set.remove(iterator)
    for s in a_set:
        print("Possible arrangement: " + s)