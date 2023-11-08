from Text.PhoneticCode import Soundex

def main():
    words = ["Soundex", "Example", "Sownteks", "Ekzampul"]
    soundex_codes = map(lambda word: (word, Soundex.soundexSimple(word)), words)
    for code in soundex_codes:
        print(code)

if __name__ == "__main__":
    main()