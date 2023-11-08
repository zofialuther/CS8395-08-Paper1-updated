```python
from OpenGL.GL import *
from OpenGL.GLUT import *

# Draw a cuboid.  Its vertices are those of a unit cube, which is then scaled
# to the required dimensions.  We only specify the visible faces, each of
# which is composed of two triangles.  The faces are rotated into position and
# rendered with a perspective transformation.

def cuboid():
    color(red)
    render(front)
    color(green)
    render(side)
    color(blue)
    render(top)

red = (1, 0, 0, 1)
green = (0, 1, 0, 1)
blue = (0, 0, 1, 1)

def render(vertices):
    glBegin(GL_TRIANGLE_STRIP)
    for vertex in vertices:
        glVertex3f(*vertex)
    glEnd()

front = [(0,0,1), (1,0,1), (0,1,1), (1,1,1)]
side = [(1,0,0), (1,1,0), (0,1,0), (0,0,1)]
top = [(0,1,1), (1,1,1), (1,1,0), (0,1,0)]

def transform():
    glTranslate(0, 0, -10)
    glRotatef(-14, 0, 0, 1)
    glRotatef(-30, 0, 1, 0)
    glRotatef(25, 1, 0, 0)
    glScalef(2, 3, 4)
    glTranslate(-0.5, -0.5, -0.5)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(40, 1, 1, 15)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    transform()
    cuboid()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutCreateWindow(b"Cuboid")
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
```