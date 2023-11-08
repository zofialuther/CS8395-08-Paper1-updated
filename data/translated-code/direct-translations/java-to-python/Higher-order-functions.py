from javax.swing import JButton, JFrame
from java.awt import BorderLayout
from java.awt.event import ActionListener, ActionEvent

class ListenerTest:
    @staticmethod
    def main(args):
        testButton = JButton("Test Button")
        testButton.addActionListener(ActionListener(){
            def actionPerformed(self, ae):
                print("Click Detected by Anon Class")
        })

        testButton.addActionListener(lambda e: print("Click Detected by Lambda Listner"))

        # Swing stuff
        frame = JFrame("Listener Test")
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        frame.add(testButton, BorderLayout.CENTER)
        frame.pack()
        frame.setVisible(True)