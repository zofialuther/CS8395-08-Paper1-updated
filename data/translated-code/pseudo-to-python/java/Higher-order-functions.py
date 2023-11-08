```python
import javax.swing.JButton;
import javax.swing.JFrame;
import java.awt.BorderLayout;
import java.awt.event.ActionListener;

class ListenerTest:
  
    def main():
        testButton = JButton("Test Button")
        
        testButton.addActionListener(new ActionListener() {
            def actionPerformed(e):
                print("Click Detected by Anon Class")
            })
        
        testButton.addActionListener(lambda e: print("Click Detected by Lambda Listener"))
        
        frame = JFrame("Listener Test")
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        frame.add(testButton, BorderLayout.CENTER)
        frame.pack()
        frame.setVisible(True)
```