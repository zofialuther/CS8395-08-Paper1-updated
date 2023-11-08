class PermutationGenerator:
    def __init__(self, size, start):
        self.size = size
        self.start = start
        self.current_permutation = start

    def reset_permutation(self):
        self.current_permutation = self.start

    def has_more_permutations(self):
        return self.current_permutation < self.start + self.size

    def get_next_permutation(self):
        if self.has_more_permutations():
            result = self.current_permutation
            self.current_permutation += 1
            return result
        else:
            return None

if __name__ == "__main__":
    pg = PermutationGenerator(3, 1)
    while pg.has_more_permutations():
        print(pg.get_next_permutation())