animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
animal_characters = ['Sociable', 'Hardworking', 'Brave', 'Cautious', 'Confident', 'Intelligent', 'Adaptable', 'Kind', 'Innovative', 'Industrious', 'Loyal', 'Sincere']
element_characters = ['Progressive', 'Dynamic', 'Stable', 'Enduring', 'Innovative']
years = [2020, 2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029]

def determine_animal(year):
    return animals[(year - 1900) % 12]

def determine_element(year):
    return elements[(year - 1900) % 10 // 2]

def determine_animal_character(year):
    return animal_characters[(year - 1900) % 12]

def determine_element_character(year):
    return element_characters[(year - 1900) % 10 // 2]

def determine_yin_or_yang(year):
    return "Yin" if (year - 1900) % 12 in [0, 2, 4, 6, 8, 10] else "Yang"

def main():
    for year in years:
        animal = determine_animal(year)
        element = determine_element(year)
        animal_character = determine_animal_character(year)
        element_character = determine_element_character(year)
        yin_or_yang = determine_yin_or_yang(year)
        print(year, element, animal, yin_or_yang, element_character, animal_character)

main()