def replicate(Term, Times, L):
    L = [Term] * Times

def replace(X, T, E, R):
    if X == 0:
        R = [E] + T[1:]
    else:
        R = [T[0]] + replace(X-1, T[1:], E, R[1:])

def replace_2d(X, Y, T, E, R):
    if Y == 0:
        R[0] = replace(X, T[0], E, R[0])
    else:
        R[0] = T[0]
        R[1:] = replace_2d(X, Y-1, T[1:], E, R[1:])

def fern_iteration(N, X, Y, I, Final):
    R = random()
    if R <= 0.01:
        X1 = 0.0
        Y1 = 0.16 * Y
    elif R <= 0.86:
        X1 = 0.85 * X + 0.04 * Y
        Y1 = -0.04 * X + 0.85 * Y + 1.6
    elif R <= 0.93:
        X1 = 0.20 * X - 0.26 * Y
        Y1 = 0.23 * X + 0.22 * Y + 1.60
    else:
        X1 = -0.15 * X + 0.28 * Y
        Y1 = 0.26 * X + 0.24 * Y + 0.44
    PointX = 250 + floor(70.0 * X1)
    PointY = 750 - floor(70.0 * Y1)
    I = replace_2d(PointX, PointY, I, [0, 255, 0], I1)
    N1 = N + 1
    fern_iteration(N1, X1, Y1, I1, Final)

def draw_fern():
    Row = [0, 0, 0] * 500
    F = [Row] * 750
    Fern = fern_iteration(0, 0, 0, F, Fern)
    File = open('fern.ppm', 'w')
    FP = [item for sublist in Fern for item in sublist]
    File.write("P6\n500 750\n255\n")
    for byte in FP:
        File.write(byte)
    File.close()