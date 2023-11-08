def generate_permutations(apartment_dwellers, s, cur_permutation):
    if s not in cur_permutation:
        next_permutation = cur_permutation + s
        if len(next_permutation) == len(apartment_dwellers):
            return [next_permutation]
        else:
            return generate_permutations(apartment_dwellers, s, next_permutation)

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

def main():
    set = set()
    permutations = generate_permutations(["B", "C", "F", "M", "S"], "", "")
    for permutation in permutations:
        if is_possible(permutation):
            set.add(permutation)
    for s in set:
        print("Possible arrangement: " + s)

if __name__ == "__main__":
    main()