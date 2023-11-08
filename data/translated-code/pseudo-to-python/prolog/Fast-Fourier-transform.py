from math import cos, sin, pi

class cx:
    def __init__(self, R, I):
        self.R = R
        self.I = I

def add(cx1, cx2):
    R = cx1.R + cx2.R
    I = cx1.I + cx2.I
    return cx(R, I)

def sub(cx1, cx2):
    R = cx1.R - cx2.R
    I = cx1.I - cx2.I
    return cx(R, I)

def mul(cx1, cx2):
    R = cx1.R * cx2.R - cx1.I * cx2.I
    I = cx1.R * cx2.I + cx2.R * cx1.I
    return cx(R, I)

def polar_cx(Mag, Theta):
    R = Mag * cos(Theta)
    I = Mag * sin(Theta)
    return cx(R, I)

def tw(Tf, Cx):
    if twiddles(Tf, Cx):
        return twiddles(Tf, Cx)
    else:
        Cx = polar_cx(1.0, -2 * pi * Tf)
        assert(twiddles(Tf, Cx))
        return Cx

def fftVals(N, Even, Odd, V0, V1):
    for K in range(len(Even)):
        E = Even[K]
        O = Odd[K]
        Tf = K / N
        Cx = tw(Tf, Cx)
        M = mul(Cx, O)
        V0 = add(E, M)
        V1 = sub(E, M)

def split(Array, Array1, Array2):
    for element in Array:
        Array1.append(element[0])
        Array2.append(element[1])

def fft(Array):
    if len(Array) == 1:
        return Array
    else:
        N = len(Array)
        EL = Array[::2]
        Even = fft(EL)
        OL = Array[1::2]
        Odd = fft(OL)
        FFTVals = fftVals(N, Even, Odd)
        L0, L1 = split(FFTVals)
        return L0 + L1

def test():
    D = [cx(1, 0), cx(1, 0), cx(1, 0), cx(1, 0), cx(0, 0), cx(0, 0), cx(0, 0), cx(0, 0)]
    DRes = fft(D)
    for element in DRes:
        R = round(element.R, 3)
        I = round(element.I, 3)
        print(R, I)