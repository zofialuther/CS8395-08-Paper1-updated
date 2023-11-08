```python
import javax.swing.*;
import java.awt.*;

public class SierpinskiCarpet extends JPanel {

    private int dim = 513;
    private int margin = 20;
    private int limit = dim;

    public SierpinskiCarpet() {
        setPreferredSize(new Dimension(dim + 2 * margin, dim + 2 * margin));
        setBackground(Color.WHITE);
        setForeground(Color.ORANGE);
        new Timer(2000, e -> {
            limit /= 3;
            if (limit <= 3) {
                limit = dim;
            }
            repaint();
        }).start();
    }

    private void drawCarpet(Graphics2D g, int x, int y, int size) {
        if (size < limit) {
            return;
        }
        size /= 3;
        for (int i = 0; i < 9; i++) {
            if (i == 4) {
                g.fillRect(x + size, y + size, size, size);
            } else {
                drawCarpet(g, x + (i % 3) * size, y + (i / 3) * size, size);
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2d.translate(margin, margin);
        drawCarpet(g2d, 0, 0, dim);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setTitle("Sierpinski Carpet");
            frame.setResizable(false);
            frame.add(new SierpinskiCarpet(), BorderLayout.CENTER);
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }

}
```