```python
import javax.swing.JFrame;
import java.awt.Graphics;

public class DragonCurve extends JFrame {
    
    public DragonCurve() {
        setTitle("Dragon Curve");
        setSize(800, 800);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
    }
    
    public void generateDragonCurve() {
        // code to generate the sequence of turns for the Dragon Curve
    }
    
    @Override
    public void paint(Graphics g) {
        // code to paint the Dragon Curve on the window using the Graphics class
    }
    
    public static void main(String[] args) {
        DragonCurve dragonCurve = new DragonCurve();
        dragonCurve.setVisible(true);
        dragonCurve.generateDragonCurve();
    }
}
```