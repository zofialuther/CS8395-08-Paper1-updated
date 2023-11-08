```python
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.swing.*;

public class YinYangGenerator extends JPanel {
    private int size;

    public YinYangGenerator(int size) {
        this.size = size;
    }

    public void drawYinYang(Graphics g) {
        int x = 0;
        int y = 0;
        g.setColor(Color.BLACK);
        g.fillOval(x, y, size, size);
        g.setColor(Color.WHITE);
        g.fillArc(x, y, size, size, 90, 180);
        g.setColor(Color.BLACK);
        g.fillArc(x, y, size, size, 270, 180);
        g.setColor(Color.WHITE);
        g.fillOval(size/4, 0, size/2, size/2);
        g.setColor(Color.BLACK);
        g.fillOval(size/4, size/2, size/2, size/2);
    }

    public BufferedImage createImage(Color bgColor) {
        BufferedImage image = new BufferedImage(size, size, BufferedImage.TYPE_INT_ARGB);
        Graphics2D g = image.createGraphics();
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g.setColor(bgColor);
        g.fillRect(0, 0, size, size);
        drawYinYang(g);
        g.dispose();
        return image;
    }

    public static void main(String[] args) {
        int size = Integer.parseInt(args[0]);
        YinYangGenerator generator = new YinYangGenerator(size);
        BufferedImage image = generator.createImage(Color.WHITE);

        JFrame frame = new JFrame();
        JLabel label = new JLabel(new ImageIcon(image));
        frame.add(label);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
    }
}
```