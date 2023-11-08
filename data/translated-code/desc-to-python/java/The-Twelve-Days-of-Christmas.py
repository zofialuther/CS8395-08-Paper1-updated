gifts = ["a Partridge in a Pear Tree", "Two Turtle Doves", "Three French Hens", "Four Calling Birds", "Five Golden Rings", "Six Geese a-Laying", "Seven Swans a-Swimming", "Eight Maids a-Milking", "Nine Ladies Dancing", "Ten Lords a-Leaping", "Eleven Pipers Piping", "Twelve Drummers Drumming"]

days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

for i in range(12):
    print(f"On the {days[i]} day of Christmas, my true love gave to me:")
    for j in range(i, -1, -1):
        if j == 0 and i != 0:
            print("and", end=" ")
        print(gifts[j])
    print("\n")