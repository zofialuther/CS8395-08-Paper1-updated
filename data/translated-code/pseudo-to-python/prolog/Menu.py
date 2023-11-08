def rosetta_menu(Items, SelectedItem):
    if not Items:
        return
    while True:
        display_menu(Items)
        choice = int(input("Select a menu item by number: "))
        if choice in range(1, len(Items) + 1):
            SelectedItem = Items[choice - 1]
            break

def display_menu(Items):
    print()
    for index, item in enumerate(Items, start=1):
        print(f"{index}) {item}")

def get_choice():
    choice = int(input("Select a menu item by number: "))
    return choice