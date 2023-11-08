```python
import java.awt.BorderLayout
import java.awt.Dimension
import java.awt.event.ActionEvent
import java.awt.event.ActionListener
import javax.swing.JButton
import javax.swing.JFrame
import javax.swing.JLabel
import javax.swing.SwingUtilities

class Clicks(JFrame):
    def __init__(self):
        super().__init__("Clicks")
        self.clicks = 0
        label = JLabel("There have been no clicks yet")
        clicker = JButton("click me")
        clicker.addActionListener(ActionListener({
            def actionPerformed(self, e):
                self.clicks += 1
                label.setText("Number of clicks: " + str(self.clicks))
        }))
        self.setLayout(BorderLayout())
        self.add(label, BorderLayout.CENTER)
        self.add(clicker, BorderLayout.SOUTH)
        label.setPreferredSize(Dimension(300, 100))
        label.setHorizontalAlignment(JLabel.CENTER)
        self.pack()
        self.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.setVisible(True)

def main():
    SwingUtilities.invokeLater(lambda: Clicks())

if __name__ == "__main__":
    main()
```