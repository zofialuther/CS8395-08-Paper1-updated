def compassangle(index, name, heading, angle):
    if angle is not None:
        resolveindex(angle, index)
        compassangle(index, name, heading, None)

def resolveindex(angle, index):
    N = angle / 11.25 + 0.5
    I = int(N)
    index = (I % 32) + 1