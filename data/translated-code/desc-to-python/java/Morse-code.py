morse_code_map = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def to_morse_code(input_string):
    morse_code = ""
    for char in input_string:
        if char.upper() in morse_code_map:
            morse_code += morse_code_map[char.upper()] + " "
    return morse_code.strip()

input1 = "Hello"
input2 = "12345"
input3 = "Goodbye"

print(to_morse_code(input1))
print(to_morse_code(input2))
print(to_morse_code(input3))