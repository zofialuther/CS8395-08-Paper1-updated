# Python code
fruits = {'apple': 1, 'banana': 2, 'cherry': 4}

def write_fruit_name(N):
    for name, quantity in fruits.items():
        if quantity == N:
            print(f'It is a {name}')

# Example usage
write_fruit_name(2)  # Output: It is a banana