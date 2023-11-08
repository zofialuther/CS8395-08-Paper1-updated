import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *

def draw_cuboid():
    # draw cuboid with visible faces using 2 triangles each
    # scale vertices to required dimensions
    # rotate faces into position
    # render with perspective transformation
    # specify colors of faces
    # display cuboid in window

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Cuboid")
    glutDisplayFunc(draw_cuboid)
    glutMainLoop()

main()