import java.awt.*;
import java.awt.image.BufferedImage;
import java.util.Random;
import javax.swing.*;

public class BarnsleyFern extends JPanel {
    private BufferedImage img;

    public BarnsleyFern() {
        int dim = 640;
        setPreferredSize(new Dimension(dim, dim));
        setBackground(Color.white);
        img = new BufferedImage(dim, dim, BufferedImage.TYPE_INT_ARGB);
        createFern(dim, dim);
    }

    private void createFern(int w, int h) {
        int x = 0, y = 0;
        Random rand = new Random();
        for (int i = 0; i < 200000; i++) {
            double r = rand.nextDouble();
            double tmpx, tmpy;
            if (r < 0.01) {
                tmpx = 0;
                tmpy = 0.16 * y;
            } else if (r < 0.86) {
                tmpx = 0.85 * x + 0.04 * y;
                tmpy = -0.04 * x + 0.85 * y + 1.6;
            } else if (r < 0.93) {
                tmpx = 0.2 * x - 0.26 * y;
                tmpy = 0.23 * x + 0.22 * y + 1.6;
            } else {
                tmpx = -0.15 * x + 0.28 * y;
                tmpy = 0.26 * x + 0.24 * y + 0.44;
            }
            x = (int) (w / 2.0 + 50 * tmpx);
            y = (int) (h - 50 * tmpy);
            img.setRGB(x, y, Color.GREEN.getRGB());
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2 = (Graphics2D) g;
        g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        g2.drawImage(img, 0, 0, this);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame frame = new JFrame();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setTitle("Barnsley Fern");
            frame.setResizable(false);
            frame.add(new BarnsleyFern(), BorderLayout.CENTER);
            frame.pack();
            frame.setLocationRelativeTo(null);
            frame.setVisible(true);
        });
    }
}