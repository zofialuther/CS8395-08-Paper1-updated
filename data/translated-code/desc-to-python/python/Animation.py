```python
import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QWidget

class Marquee(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("color: cyan; font-weight: bold;")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_text)
        self.timer.start(100)

    def move_text(self):
        pos = self.pos()
        if pos.x() < -self.width():
            self.move(self.parent().width(), pos.y())
        else:
            self.move(pos.x() - 2, pos.y())

    def mousePressEvent(self, event):
        self.timer.stop()
        if self.pos().x() < self.parent().width() / 2:
            self.timer.timeout.disconnect(self.move_text)
            self.timer.timeout.connect(self.move_text_reverse)
        else:
            self.timer.timeout.disconnect(self.move_text_reverse)
            self.timer.timeout.connect(self.move_text)
        self.timer.start(100)
    
    def move_text_reverse(self):
        pos = self.pos()
        if pos.x() > self.parent().width():
            self.move(-self.width(), pos.y())
        else:
            self.move(pos.x() + 2, pos.y())

class MarqueeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(0, 0, 400, 100)
        self.marquee = Marquee("Hello World!")
        self.marquee.setParent(self)
        self.marquee.move((self.width() - self.marquee.width()) / 2, (self.height() - self.marquee.height()) / 2)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MarqueeWindow()
    window.show()
    sys.exit(app.exec_())
```