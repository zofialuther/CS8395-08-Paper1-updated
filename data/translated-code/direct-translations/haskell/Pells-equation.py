def pell(n):
    x = int(math.floor(math.sqrt(float(n)))
    y, z, r, e1, e2, f1, f2 = x, 1, x * 2, 1, 0, 0, 1

    while True:
        y_ = r * z - y
        z_ = (n - y_ * y_) // z
        r_ = (x + y_) // z_
        e1, e2 = e2, e2 * r_ + e1
        f1, f2 = f2, f2 * r_ + f1
        a, b = f2, e2
        b_, a_ = a, a * x + b

        if a_ * a_ - n * b_ * b_ == 1:
            return a_, b_

        y, z, r = y_, z_, r_