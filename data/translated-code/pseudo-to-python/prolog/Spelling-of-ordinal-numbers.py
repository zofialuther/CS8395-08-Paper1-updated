def number_name(Number, Type, Name):
    if Number < 20:
        get_small_name(Number, Type, Name)
    elif Number < 100:
        N = Number % 10
        if N == 0:
            get_small_name(Number, Type, Name)
        else:
            N1 = Number - N
            Name1 = get_small_name(N1, "cardinal")
            Name2 = get_small_name(N, Type)
            Name = Name1 + '-' + Name2
    else:
        P, C, O = big_name(Number)
        N = Number // P
        Name1 = number_name(N, "cardinal")
        M = Number % P
        if M == 0:
            Name2 = get_big_name(big(P, C, O), Type)
        else:
            Name3 = number_name(M, Type)
            Name2 = C + ' ' + Name3
        Name = Name1 + ' ' + Name2

def get_small_name(Number, Type):
    if Type == "cardinal":
        Name = small_name_dict[Number][0]
    else:
        Name = small_name_dict[Number][1]
    return Name

def get_big_name(big, Type):
    if Type == "cardinal":
        return big[1]
    else:
        return big[2]

def big_name(Number):
    Names = big_name_dict
    for i in range(len(Names)):
        if i == len(Names) - 1:
            return Names[i][1]
        elif Number < Names[i+1][0]:
            return Names[i][1]

small_name_dict = {
    1: ("one", "first"),
    2: ("two", "second"),
    3: ("three", "third"),
    4: ("four", "fourth"),
    5: ("five", "fifth"),
    6: ("six", "sixth"),
    7: ("seven", "seventh"),
    8: ("eight", "eighth"),
    9: ("nine", "ninth"),
    10: ("ten", "tenth"),
    11: ("eleven", "eleventh"),
    12: ("twelve", "twelfth"),
    13: ("thirteen", "thirteenth"),
    14: ("fourteen", "fourteenth"),
    15: ("fifteen", "fifteenth"),
    16: ("sixteen", "sixteenth"),
    17: ("seventeen", "seventeenth"),
    18: ("eighteen", "eighteenth"),
    19: ("nineteen", "nineteenth")
}

big_name_dict = [
    (100, ("hundred", "hundredth")),
    (1000, ("thousand", "thousandth")),
    (1000000, ("million", "millionth")),
    (1000000000, ("billion", "billionth")),
    (1000000000000, ("trillion", "trillionth"))
]