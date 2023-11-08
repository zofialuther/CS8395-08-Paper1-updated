class LinePlaneIntersection:
    class Vector3D:
        def __init__(self, x, y, z):
            self.x = x
            self.y = y
            self.z = z
        
        def plus(self, v):
            return Vector3D(self.x + v.x, self.y + v.y, self.z + v.z)
        
        def minus(self, v):
            return Vector3D(self.x - v.x, self.y - v.y, self.z - v.z)
        
        def times(self, s):
            return Vector3D(s * self.x, s * self.y, s * self.z)
        
        def dot(self, v):
            return self.x * v.x + self.y * v.y + self.z * v.z
        
        def __str__(self):
            return f"({self.x}, {self.y}, {self.z})"
    
    @staticmethod
    def intersectPoint(rayVector, rayPoint, planeNormal, planePoint):
        diff = rayPoint.minus(planePoint)
        prod1 = diff.dot(planeNormal)
        prod2 = rayVector.dot(planeNormal)
        prod3 = prod1 / prod2
        return rayPoint.minus(rayVector.times(prod3))
    
    @staticmethod
    def main():
        rv = LinePlaneIntersection.Vector3D(0.0, -1.0, -1.0)
        rp = LinePlaneIntersection.Vector3D(0.0, 0.0, 10.0)
        pn = LinePlaneIntersection.Vector3D(0.0, 0.0, 1.0)
        pp = LinePlaneIntersection.Vector3D(0.0, 0.0, 5.0)
        ip = LinePlaneIntersection.intersectPoint(rv, rp, pn, pp)
        print("The ray intersects the plane at", ip)

LinePlaneIntersection.main()