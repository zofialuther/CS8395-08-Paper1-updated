gifts = [
    "A partridge in a pear tree.", "Two turtle doves and",
    "Three french hens", "Four calling birds",
    "Five golden rings", "Six geese a-laying",
    "Seven swans a-swimming", "Eight maids a-milking",
    "Nine ladies dancing", "Ten lords a-leaping",
    "Eleven pipers piping", "Twelve drummers drumming",
    "And a partridge in a pear tree.", "Two turtle doves"
]

days = [
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh",
    "eighth", "ninth", "tenth", "eleventh", "Twelfth"
]

def main():
    for i in range(len(days)):
        print("\nOn the", days[i], "day of Christmas")
        print("My true love gave to me:")
        for j in range(i, -1, -1):
            print(gifts[i if i != 11 or j >= 2 else j + 12])

main()