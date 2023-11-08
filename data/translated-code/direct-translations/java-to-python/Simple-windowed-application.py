import javax.swing
from java.awt import BorderLayout, Dimension, event
from java.awt.event import ActionListener
from javax.swing import JButton, JFrame, JLabel, SwingUtilities

class Clicks(JFrame):
    def __init__(self):
        super().__init__("Clicks")  # set window title
        self.clicks = 0
        label = JLabel("There have been no clicks yet")
        clicker = JButton("click me")
        
        def button_listener(e):
            nonlocal clicks
            self.clicks += 1
            label.setText("There have been " + str(self.clicks) + " clicks")  # change the text
        
        clicker.addActionListener(ActionListener(button_listener))  # listen to the button
        self.setLayout(BorderLayout())  # handles placement of components
        self.add(label, BorderLayout.CENTER)  # add the label to the biggest section
        self.add(clicker, BorderLayout.SOUTH)  # put the button underneath it
        label.setPreferredSize(Dimension(300, 100))  # nice big label
        label.setHorizontalAlignment(JLabel.CENTER)  # text not up against the side
        self.pack()  # fix layout
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)  # stop the program on "X"
        self.setVisible(True)  # show it

    @staticmethod
    def main(args):
        SwingUtilities.invokeLater(lambda: Clicks())  # call the constructor where all the magic happens
```