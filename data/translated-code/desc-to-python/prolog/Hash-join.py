people = [
    {'name': 'Alice', 'age': 25, 'character': 'brave', 'nemesis': 'dragon'},
    {'name': 'Bob', 'age': 30, 'character': 'clever', 'nemesis': 'witch'},
    {'name': 'Charlie', 'age': 20, 'character': 'kind', 'nemesis': 'giant'}
]

def join_and_print(people):
    for person in people:
        print(f"{person['name']} is {person['age']} years old, and is {person['character']}. Their nemesis is {person['nemesis']}.")

join_and_print(people)