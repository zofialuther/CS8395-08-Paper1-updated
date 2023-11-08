class Zodiac:
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    elements = ["Wood", "Fire", "Earth", "Metal", "Water"]
    characters = ["Yang", "Yin"]

    def yin_or_yang(self, year):
        if year % 2 == 0:
            return "Yang"
        else:
            return "Yin"

    def determine_zodiac_sign(self, year):
        animal_index = (year - 4) % 12
        element_index = (year - 4) % 10
        character = self.yin_or_yang(year)
        print(f"{year} is the year of the {self.elements[element_index]} {self.animals[animal_index]}, which is a {character} year.")

if __name__ == "__main__":
    zodiac = Zodiac()
    years = [1980, 1993, 2008, 2022]
    for year in years:
        zodiac.determine_zodiac_sign(year)