def intersectPoint(rayVector, rayPoint, planeNormal, planePoint):
    diff = rayPoint - planePoint
    prod1 = diff.dot(planeNormal)
    prod2 = rayVector.dot(planeNormal)
    prod3 = prod1 / prod2
    return rayPoint - (rayVector * prod3)

def main(args):
    rv = Vector3D(0.0, -1.0, -1.0)
    rp = Vector3D(0.0, 0.0, 10.0)
    pn = Vector3D(0.0, 0.0, 1.0)
    pp = Vector3D(0.0, 0.0, 5.0)
    ip = intersectPoint(rv, rp, pn, pp)
    print("The ray intersects the plane at ", ip)