import sys
import morse_code
import morse_play_sox

# Read standard input, converting text to Morse code, then playing the result.
# We turn off buffering on stdin so it will play as you type.
def main():
    sys.stdin = open(0)
    text = sys.stdin.read()
    morse_text = morse_code.to_morse(text)
    morse_play_sox.play(morse_text)

if __name__ == "__main__":
    main()