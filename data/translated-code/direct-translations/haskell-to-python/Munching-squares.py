from data import bits
import bytestring as BY

def main():
    BY.writeFile("out.pgm", BY.pack(
        list(map(lambda x: int(ord(x)), "P5\n256 256\n256\n")) +
        [x ^ y for x in range(256) for y in range(256)]
    ))