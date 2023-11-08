import javax.swing.*;
import java.awt.*;

public class SierpinskyTriangle extends JPanel {
    
    private int level;

    public SierpinskyTriangle(int level) {
        this.level = level;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawSierpinskyTriangle(g, level, 50, 50, 500, 500);
    }

    private void drawSierpinskyTriangle(Graphics g, int level, int x1, int y1, int x2, int y2) {
        if (level == 0) {
            int[] xPoints = {x1, (x1 + x2) / 2, x2};
            int[] yPoints = {y2, y1, y2};
            g.drawPolygon(xPoints, yPoints, 3);
        } else {
            int mid1x = (x1 + x2) / 2;
            int mid2x = (x1 + x2) / 2;
            int midy = (y1 + y2) / 2;

            drawSierpinskyTriangle(g, level - 1, x1, y1, mid2x, midy);
            drawSierpinskyTriangle(g, level - 1, mid1x, y1, x2, midy);
            drawSierpinskyTriangle(g, level - 1, mid1x, midy, mid2x, y2);
        }
    }

    public static void main(String[] args) {
        int level = 3;
        if (args.length > 0) {
            level = Integer.parseInt(args[0]);
        }

        JFrame frame = new JFrame("Sierpinsky Triangle");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new SierpinskyTriangle(level));
        frame.setSize(600, 600);
        frame.setVisible(true);
    }
}