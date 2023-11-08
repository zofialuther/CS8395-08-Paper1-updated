def select_string_from_list(strings, prompt):
    if not strings:
        return ""
    
    while True:
        for i, string in enumerate(strings):
            print(f"{i}: {string}")
        
        index = input(prompt)
        try:
            index = int(index)
            if 0 <= index < len(strings):
                return strings[index]
            else:
                print("Invalid index. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")