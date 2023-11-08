def main(args):
    if len(args) >= 1:
        for file in args:
            try:
                with open(file, 'r') as f:
                    content = f.read()
                    result = rot13(content)
                    print(result)
            except FileNotFoundError:
                print("File not found")
    else:
        content = input("Enter text: ")
        result = rot13(content)
        print(result)

def rot13(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char
    return result

# Example usage
main(["input.txt"])