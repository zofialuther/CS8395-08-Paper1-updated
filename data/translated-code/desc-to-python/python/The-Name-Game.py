def print_verse(name):
    if name[0].lower() in ['a', 'e', 'i', 'o', 'u']:
        modified_name = name.lower()
    elif name[0].lower() in ['g', 'b', 'f']:
        modified_name = name[1:]
    else:
        modified_name = name
    
    print(f"{modified_name}, {modified_name}, bo-b{modified_name[1:]}")
    print(f"Banana-fana fo-f{modified_name[1:]}")
    print(f"Fee-fi-mo-m{modified_name[1:]}")
    print(f"{modified_name}!")
    
names = ['Gary', 'Earl', 'Billy', 'Felix', 'Mary']
for name in names:
    print_verse(name)