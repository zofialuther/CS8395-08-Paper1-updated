animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
animal_chars = ['鼠', '牛', '虎', '兔', '龙', '蛇', '马', '羊', '猴', '鸡', '狗', '猪']
element_chars = ['木', '火', '土', '金', '水']
years = [2020, 2021, 2022, 2023, 2024, 2025]  # Add more years as needed

def zodiac_info(year):
    animal = animals[(year - 1900) % 12]
    element = elements[(year - 1900) % 10 // 2]
    yin_yang = 'Yang' if (year - 1900) // 2 % 2 == 0 else 'Yin'
    print(f'{year}: Animal - {animal}, Element - {element}, Yin/Yang - {yin_yang}')

for year in years:
    zodiac_info(year)