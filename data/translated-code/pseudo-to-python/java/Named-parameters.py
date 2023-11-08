from typing import Optional

class NutritionFacts:
    class Builder:
        def __init__(self, serving_size: int, servings: int):
            self.serving_size = serving_size
            self.servings = servings
            self.calories: Optional[int] = None
            self.sodium: Optional[int] = None
            self.carbohydrate: Optional[int] = None
            
        def set_calories(self, calories: int):
            self.calories = calories
            return self
            
        def set_sodium(self, sodium: int):
            self.sodium = sodium
            return self
            
        def set_carbohydrate(self, carbohydrate: int):
            self.carbohydrate = carbohydrate
            return self
            
        def build(self):
            return NutritionFacts(self)
    
    def __init__(self, builder: Builder):
        self.serving_size = builder.serving_size
        self.servings = builder.servings
        self.calories = builder.calories
        self.sodium = builder.sodium
        self.carbohydrate = builder.carbohydrate

# Start
builder = NutritionFacts.Builder(240, 8)
builder.set_calories(100)
builder.set_sodium(35)
builder.set_carbohydrate(27)
nutrition_facts = builder.build()
# End