from math import cos, sin, pi

def unity(n):
    print('\n{}: '.format(n))

    for angle in range(0, int(2 * pi), int((2 * pi) / n)):
        real = cos(angle) 
        if abs(real) < 1.0E-3:
            real = 0.0 

        imag = sin(angle) 
        if abs(imag) < 1.0E-3:
            imag = 0.0

        print('(%9f,%9f) '.format(real, imag))

def main():
    for n in range(2, 6):
        unity(n)

main()