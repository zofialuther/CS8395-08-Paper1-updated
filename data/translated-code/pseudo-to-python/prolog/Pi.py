def pi_spigot():
    X = pi()
    for Y in X:
        print(Y)

def pi(OUT):
    pi(1, 180, 60, 2, OUT)

def pi(Q, R, T, I, OUT):
    if OUT.frozen:
        if not OUT.empty:
            U = 3 * (3 * I + 1) * (3 * I + 2)
            Y = (Q * (27 * I - 12) + 5 * R) // (5 * T)
            Digit = Y
            Q2 = 10 * Q * I * (2 * I - 1)
            R2 = 10 * U * (Q * (5 * I - 2) + R - Y * T)
            T2 = T * U
            I2 = I + 1
            pi(Q2, R2, T2, I2, OUT_)
        else:
            return True