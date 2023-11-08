class NutritionFactsBuilder:
    def __init__(self):
        self.serving_size = None
        self.servings_per_container = None
        self.calories = None
        self.sodium = None
        self.carbohydrates = None

    def set_serving_size(self, serving_size):
        self.serving_size = serving_size
        return self

    def set_servings_per_container(self, servings_per_container):
        self.servings_per_container = servings_per_container
        return self

    def set_calories(self, calories):
        self.calories = calories
        return self

    def set_sodium(self, sodium):
        self.sodium = sodium
        return self

    def set_carbohydrates(self, carbohydrates):
        self.carbohydrates = carbohydrates
        return self

    def build(self):
        return NutritionFacts(self)