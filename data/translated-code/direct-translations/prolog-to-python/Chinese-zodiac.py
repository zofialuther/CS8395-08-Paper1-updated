```python
def main():
    def year_animal(Year):
        I = ((Year - 4) % 12) + 1
        Animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']
        return Animals[I - 1]
    
    def year_element(Year):
        I = ((Year - 4) % 10) // 2 + 1
        Elements = ['Wood', 'Fire', 'Earth', 'Metal', 'Water']
        return Elements[I - 1]
    
    def year_animal_char(Year):
        I = (Year - 4) % 12 + 1
        AnimalChars = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
        return AnimalChars[I - 1]
    
    def year_element_char(Year):
        I1 = Year % 2 + 1
        ElementChars = [['甲', '丙', '戊', '庚', '壬'], ['乙', '丁', '己', '辛', '癸']]
        ElementChars1 = ElementChars[I1 - 1]
        I2 = (Year - 4) % 10 // 2 + 1
        return ElementChars1[I2 - 1]
    
    def year_yin_yang(Year):
        return 'yang' if Year % 2 == 0 else 'yin'
    
    Years = [1935, 1938, 1968, 1972, 1976, 1984, 1985, 2017]
    for Year in Years:
        print(Year, 'is the year of the', year_element(Year), year_animal(Year), year_yin_yang(Year), '(' + year_element_char(Year) + year_animal_char(Year) + ')')

if __name__ == "__main__":
    main()
```