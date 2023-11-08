import sys
from MorseCode import toMorse
from MorsePlaySox import play

def main():
    sys.stdin = open(0)
    input_text = sys.stdin.read()
    morse_code = toMorse(input_text)
    play(morse_code)