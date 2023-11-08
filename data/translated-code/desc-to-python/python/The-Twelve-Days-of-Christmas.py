gifts = ["a partridge in a pear tree", "two turtle doves", "three French hens", "four calling birds", "five golden rings", "six geese a-laying", "seven swans a-swimming", "eight maids a-milking", "nine ladies dancing", "ten lords a-leaping", "eleven pipers piping", "twelve drummers drumming"]
days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

for i in range(12):
    print(f"On the {days[i]} day of Christmas, my true love gave to me:")
    for j in range(i, -1, -1):
        if j == 0 and i != 0:
            print(f"And {gifts[j]}")
        else:
            print(f"{gifts[j]}")
    print("\n")