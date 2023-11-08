```python
import javax.swing.*;
import java.awt.*;

public class XORPattern extends JPanel {
  
  public void paintComponent(Graphics g) {
    super.paintComponent(g);
    for (int x = 0; x < getWidth(); x++) {
      for (int y = 0; y < getHeight(); y++) {
        int colorValue = (x ^ y) * 255 / (getWidth() + getHeight());
        g.setColor(new Color(colorValue, colorValue, colorValue));
        g.drawLine(x, y, x, y);
      }
    }
  }
  
  public static void main(String[] args) {
    JFrame frame = new JFrame("XOR Pattern");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.add(new XORPattern());
    frame.setSize(400, 400);
    frame.setVisible(true);
  }
}
```