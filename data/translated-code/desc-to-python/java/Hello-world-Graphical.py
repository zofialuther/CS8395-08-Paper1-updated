```python
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JTextArea;
import javax.swing.JButton;
import java.awt.FlowLayout;

public class HelloWorldGUI extends JFrame {

  public HelloWorldGUI() {
    setTitle("Hello, World!");
    setSize(300, 200);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    setLayout(new FlowLayout());

    JOptionPane.showMessageDialog(this, "Goodbye, World!");
    
    JTextArea textArea = new JTextArea("Goodbye, World!");
    add(textArea);
    
    JButton button = new JButton("Goodbye, World!");
    add(button);
    
    setVisible(true);
  }

  public static void main(String[] args) {
    new HelloWorldGUI();
  }
}
```