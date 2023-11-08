import javax.swing.JFrame
import javax.swing.JLabel
import javax.swing.WindowConstants
from java.awt.event import MouseAdapter, MouseEvent, WindowAdapter, WindowEvent
from java.util import Timer, TimerTask

class State:
    def __init__(self):
        self.text = "Hello World! "
        self.startIndex = 0
        self.rotateRight = True

def main():
    state = State()

    label = JLabel(state.text)
    label.addMouseListener(MouseAdapter() {
        def mouseClicked(event):
            state.rotateRight = not state.rotateRight
    })

    task = TimerTask() {
        def run():
            delta = 1 if state.rotateRight else -1
            state.startIndex = (state.startIndex + len(state.text) + delta) % len(state.text)
            label.setText(rotate(state.text, state.startIndex))
    }
    timer = Timer(False)
    timer.schedule(task, 0, 500)

    rot = JFrame()
    rot.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE)
    rot.add(label)
    rot.pack()
    rot.setLocationRelativeTo(None)
    rot.addWindowListener(WindowAdapter() {
        def windowClosed(e):
            timer.cancel()
    })
    rot.setVisible(True)

def rotate(text, startIdx):
    rotated = [None] * len(text)
    for i in range(len(text)):
        rotated[i] = text[(i + startIdx) % len(text)]
    return ''.join(rotated)

if __name__ == "__main__":
    main()