def uppersAndLowers():
    characters = [chr(i) for i in range(1, 0x110000)]
    printable_chars = list(filter(lambda x: x.isprintable(), characters))
    lower_chars = list(filter(lambda x: x.islower(), printable_chars))
    upper_chars = list(filter(lambda x: x.isupper(), printable_chars))
    return lower_chars, upper_chars

def main():
    lower, upper = uppersAndLowers()
    lower_chunks = [lower[i:i+70] for i in range(0, len(lower), 70)]
    upper_chunks = [upper[i:i+70] for i in range(0, len(upper), 70)]
    lower_str = "Lower:" + '\n'.join(lower_chunks)
    upper_str = "Upper:" + '\n'.join(upper_chunks)
    print(upper_str + "\n" + lower_str)