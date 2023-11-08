```python
import sys
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class Marquee(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initUI()
        self.timer = QBasicTimer()
        self.timer.start(100, self)

    def initUI(self):
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setText("This is a marquee")
        self.setFont(QFont("Arial", 20))
        self.setStyleSheet("color: red")

    def timerEvent(self, event):
        if event.timerId() == self.timer.timerId():
            self.setText(self.text()[1:] + self.text()[0])

    def mouseReleaseEvent(self, event):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

app = QApplication(sys.argv)
marquee = Marquee()
marquee.resize(300, 100)
marquee.move(400, 300)
marquee.show()
sys.exit(app.exec_())
```