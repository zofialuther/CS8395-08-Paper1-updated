gifts = [
    "And a partridge in a pear tree!",
    "Two turtle doves,",
    "Three french hens,",
    "Four calling birds,",
    "FIVE GOLDEN RINGS,",
    "Six geese a-laying,",
    "Seven swans a-swimming,",
    "Eight maids a-milking,",
    "Nine ladies dancing,",
    "Ten lords a-leaping,",
    "Eleven pipers piping,",
    "Twelve drummers drumming"
]

days = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth"
]

def verseOfTheDay(day):
    print("On the", days[day], "day of Christmas my true love gave to me... ")
    for d in range(day, -1, -1):
        if d == 0:
            print("A partridge in a pear tree!")
        else:
            print(gifts[d])
    print("")

def main():
    for day in range(12):
        verseOfTheDay(day)

main()