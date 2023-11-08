def person_age(name, age):
    return (name, age)

def character_nemesis(name, nemesis):
    return (name, nemesis)

def join_and_print():
    print('Age\tName\tCharacter\tNemisis\n')
    people = ['Jonah', 'Alan', 'Glory', 'Popeye']
    for person in people:
        for nemesis in ['Whales', 'Spiders', 'Ghosts', 'Zombies', 'Buffy']:
            if (person, nemesis) in [('Jonah', 'Whales'), ('Jonah', 'Spiders'), ('Alan', 'Ghosts'), ('Alan', 'Zombies'), ('Glory', 'Buffy')]:
                age = [27, 18, 28, 18][people.index(person)]
                print(f'{age}\t{person}\t{person}\t\t{nemesis}')

join_and_print()