def calculate_hypotenuse(a, b):
    return (a ** 2 + b ** 2) ** 0.5

def generate_general_triples():
    for a in range(1, 100):
        for b in range(a, 100):
            c = calculate_hypotenuse(a, b)
            if c == int(c):
                print(f"Pythagorean triple: {a}, {b}, {int(c)}")

def generate_specific_triples():
    for a in range(1, 100):
        for b in range(1, 100):
            c = calculate_hypotenuse(a, b)
            if c == int(c):
                print(f"Pythagorean triple: {a}, {b}, {int(c)}")

if __name__ == "__main__":
    print("Generating Pythagorean triples for general cases:")
    generate_general_triples()
    print("\nGenerating Pythagorean triples for specific cases:")
    generate_specific_triples()