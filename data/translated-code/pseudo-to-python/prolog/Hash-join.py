def person_age(name, age):
    person_age[name] = age

def character_nemisis(name, nemesis):
    character_nemisis[name] = nemesis

def join_and_print():
    print('Age\tName\tCharacter\tNemisis\n')
    for person in person_age:
        age = person_age[person]
        nemesis = character_nemisis[person]
        print(f'{age}\t{person}\t{person}\t\t{nemesis}')