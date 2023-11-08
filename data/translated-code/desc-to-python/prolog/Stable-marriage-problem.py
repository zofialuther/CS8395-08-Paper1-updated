class Person:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.engaged_to = None

def stable_marriage(men, women):
    # implementation of Gale-Shapley algorithm
    pass

def is_stable(couples):
    # check if the matches are stable
    pass

def perturb_couples(couples):
    # perturb the couples to test stability
    pass

# define men and women with their preferences
men = {
    'John': ['Emily', 'Anna', 'Sophia'],
    'Michael': ['Sophia', 'Emily', 'Anna'],
    'David': ['Anna', 'Sophia', 'Emily']
}

women = {
    'Emily': ['Michael', 'David', 'John'],
    'Anna': ['David', 'John', 'Michael'],
    'Sophia': ['John', 'Michael', 'David']
}

# create Person objects for each man and woman
men_objects = [Person(name, men[name]) for name in men]
women_objects = [Person(name, women[name]) for name in women]

# find stable matches using Gale-Shapley algorithm
stable_matches = stable_marriage(men_objects, women_objects)

# test the stability of the matches
is_stable(stable_matches)

# perturb the couples to test their stability
perturb_couples(stable_matches)