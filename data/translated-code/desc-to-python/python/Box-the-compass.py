cardinal_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW', 'N']
compass_divisions = 360 / len(cardinal_directions)

def degrees2compasspoint(degrees):
    index = int((degrees / compass_divisions) + 0.5) % len(cardinal_directions)
    return cardinal_directions[index]

for degree in range(0, 360, 45):
    print(f"{degree} degrees is {degrees2compasspoint(degree)}")