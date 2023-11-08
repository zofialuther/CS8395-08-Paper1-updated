from diagrams import Diagram, DiagramNode

def triangle(size):
    return Diagram().add_triagle(size).fill("black").outline("none")

def reduce(triangle1, triangle2, triangle3):
    return Diagram().stack(triangle1, triangle2, triangle3)

def sierpinski(iterations):
    if iterations == 0:
        return triangle(100)
    else:
        smaller_triangles = sierpinski(iterations - 1)
        return reduce(smaller_triangles, smaller_triangles, smaller_triangles)

def main():
    sierpinski_triangle = sierpinski(7)
    sierpinski_triangle.defaultMain()