```python
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Graphics;

public class BresenhamLineDrawing extends JFrame {
    public BresenhamLineDrawing() {
        setTitle("Bresenham Line Drawing");
        setSize(800, 600);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        add(new BresenhamPanel());
    }
    
    public static void main(String[] args) {
        BresenhamLineDrawing app = new BresenhamLineDrawing();
        app.setVisible(true);
    }
}

class BresenhamPanel extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawLine(g, 100, 100, 200, 100);
        drawLine(g, 100, 100, 100, 200);
        drawLine(g, 100, 100, 200, 200);
        drawLine(g, 200, 100, 100, 200);
        drawLine(g, 200, 100, 200, 200);
        drawLine(g, 100, 200, 200, 200);
        drawLine(g, 200, 200, 100, 200);
        drawLine(g, 150, 100, 150, 200);
    }
    
    private void drawLine(Graphics g, int x1, int y1, int x2, int y2) {
        int dx = Math.abs(x2 - x1);
        int dy = Math.abs(y2 - y1);
        int sx = (x1 < x2) ? 1 : -1;
        int sy = (y1 < y2) ? 1 : -1;
        int err = dx - dy;
        
        while (true) {
            plot(g, x1, y1);
            if (x1 == x2 && y1 == y2) {
                break;
            }
            int e2 = 2 * err;
            if (e2 > -dy) {
                err -= dy;
                x1 += sx;
            }
            if (e2 < dx) {
                err += dx;
                y1 += sy;
            }
        }
    }
    
    private void plot(Graphics g, int x, int y) {
        g.fillRect(x, y, 1, 1);
    }
}
```