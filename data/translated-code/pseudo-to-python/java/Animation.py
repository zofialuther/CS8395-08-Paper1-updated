class State:
    def __init__(self, text, startIndex, rotateRight):
        self.text = text
        self.startIndex = startIndex
        self.rotateRight = rotateRight

def main():
    state = State("example text", 0, False)
    label = JLabel(state.text)
    label.addMouseListener(MouseAdapter() {
        def mouseClicked(self, e):
            state.rotateRight = not state.rotateRight
    })
    task = TimerTask() {
        def run(self):
            rotate(state)
            label.setText(state.text)
    }
    timer = Timer()
    timer.schedule(task, 0, 500)
    frame = JFrame()
    frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE)
    frame.add(label)
    frame.pack()
    frame.setLocationRelativeTo(None)
    frame.addWindowListener(WindowAdapter() {
        def windowClosed(self, e):
            timer.cancel()
    })
    frame.setVisible(True)

def rotate(state):
    if state.rotateRight:
        state.text = state.text[-1] + state.text[:-1]
    else:
        state.text = state.text[1:] + state.text[0]