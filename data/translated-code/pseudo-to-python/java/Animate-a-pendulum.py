class Pendulum(JPanel, Runnable):
    angle = math.pi / 2
    length = 0

    def __init__(self, length):
        self.length = length
        self.setDoubleBuffered(True)

    def paint(self, g):
        g.setColor(Color.WHITE)
        g.fillRect(0, 0, self.getWidth(), self.getHeight())
        g.setColor(Color.BLACK)
        anchorX = self.getWidth() / 2
        anchorY = self.getHeight() / 4
        ballX = anchorX + int(math.sin(self.angle) * self.length)
        ballY = anchorY + int(math.cos(self.angle) * self.length)
        g.drawLine(anchorX, anchorY, ballX, ballY)
        g.fillOval(anchorX - 3, anchorY - 4, 7, 7)
        g.fillOval(ballX - 7, ballY - 7, 14, 14)

    def run(self):
        angleAccel = 0
        angleVelocity = 0
        dt = 0.1
        while True:
            angleAccel = -9.81 / self.length * math.sin(self.angle)
            angleVelocity += angleAccel * dt
            self.angle += angleVelocity * dt
            self.repaint()
            try:
                Thread.sleep(15)
            except InterruptedException:
                pass

    def getPreferredSize(self):
        return Dimension(2 * self.length + 50, self.length // 2 * 3)

    def main(self, args):
        f = JFrame("Pendulum")
        p = Pendulum(200)
        f.add(p)
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        f.pack()
        f.setVisible(True)
        Thread(p).start()