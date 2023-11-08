import sys
import MorsePlaySox

def main():
    sys.stdin = open(0)
    text = input("Enter text to convert to Morse code: ")
    morse_code = MorsePlaySox.text_to_morse(text)
    MorsePlaySox.play_morse(morse_code)

if __name__ == "__main__":
    main()