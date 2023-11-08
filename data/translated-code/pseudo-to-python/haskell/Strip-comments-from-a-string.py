ms = ";#"

def main(input):
    for line in input:
        result = ""
        for char in line:
            if char not in ms:
                result += char
            else:
                break
        print(result)

# End of main.