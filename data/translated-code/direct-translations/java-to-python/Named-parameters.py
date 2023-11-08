class NutritionFacts:
    def __init__(self, serving_size, servings):
        self.serving_size = serving_size
        self.servings = servings
        self.calories = 0
        self.sodium = 0
        self.carbohydrate = 0

    def calories(self, calories):
        self.calories = calories
        return self

    def sodium(self, sodium):
        self.sodium = sodium
        return self

    def carbohydrate(self, carbohydrate):
        self.carbohydrate = carbohydrate
        return self

    def build(self):
        return self

new_nutrition_facts = NutritionFacts(240, 8).calories(100).sodium(35).carbohydrate(27).build()
processNutritionFacts(new_nutrition_facts)