import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Cuboid:
    def __init__(self):
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_box_aspect([1,1,1])  # aspect ratio is 1:1:1

        self.nodes = np.array([[-1, -1, -1], [-1, -1, 1], [-1, 1, -1], [-1, 1, 1],
                               [1, -1, -1], [1, -1, 1], [1, 1, -1], [1, 1, 1]])

        self.edges = [(0, 1), (1, 3), (3, 2), (2, 0), (4, 5), (5, 7), (7, 6),
                      (6, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

        self.mouseX, self.prevMouseX, self.mouseY, self.prevMouseY = 0, 0, 0, 0

        self.scale(80, 120, 160)
        self.rotateCube(math.pi / 5, math.pi / 9)

    def scale(self, sx, sy, sz):
        for node in self.nodes:
            node[0] *= sx
            node[1] *= sy
            node[2] *= sz

    def rotateCube(self, angleX, angleY):
        rotation_matrix_x = np.array([[1, 0, 0],
                                      [0, math.cos(angleX), -math.sin(angleX)],
                                      [0, math.sin(angleX), math.cos(angleX)]])

        rotation_matrix_y = np.array([[math.cos(angleY), 0, math.sin(angleY)],
                                      [0, 1, 0],
                                      [-math.sin(angleY), 0, math.cos(angleY)])

        for i in range(len(self.nodes)):
            self.nodes[i] = np.dot(rotation_matrix_x, self.nodes[i])
            self.nodes[i] = np.dot(rotation_matrix_y, self.nodes[i])

    def drawCube(self):
        for edge in self.edges:
            x = [self.nodes[edge[0]][0], self.nodes[edge[1]][0]]
            y = [self.nodes[edge[0]][1], self.nodes[edge[1]][1]]
            z = [self.nodes[edge[0]][2], self.nodes[edge[1]][2]]
            self.ax.plot(x, y, z, color='b')

        for node in self.nodes:
            self.ax.scatter(node[0], node[1], node[2], color='r')

    def showCube(self):
        self.drawCube()
        plt.show()

cuboid = Cuboid()
cuboid.showCube()