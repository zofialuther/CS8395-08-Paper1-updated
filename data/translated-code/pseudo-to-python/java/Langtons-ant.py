```python
import javax.swing.JFrame;
import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Graphics;

public class Langton extends JFrame {
    private JPanel planePanel;
    private static final int ZOOM = 4;

    public Langton(boolean[][] plane) {
        planePanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                for (int y = 0; y < plane.length; y++) {
                    for (int x = 0; x < plane[y].length; x++) {
                        if (plane[y][x]) {
                            g.setColor(Color.BLACK);
                        } else {
                            g.setColor(Color.WHITE);
                        }
                        g.fillRect(x * ZOOM, y * ZOOM, ZOOM, ZOOM);
                    }
                }
                g.setColor(Color.GREEN);
                g.fillRect((plane[0].length - 1) * ZOOM / 2, (plane.length - 1) * ZOOM / 2, ZOOM / 2, ZOOM / 2);
            }
        };
        planePanel.setSize(plane[0].length - 1, plane.length - 1);
        add(planePanel);
        setSize(ZOOM * plane[0].length, ZOOM * plane.length + 30);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        boolean[][] plane = runAnt(100, 100);
        new Langton(plane);
    }

    public static boolean[][] runAnt(int height, int width) {
        boolean[][] plane = new boolean[height][width];
        int antX = width / 2;
        int antY = height / 2;
        int xChange = 0;
        int yChange = -1;
        while (antX < width && antY < height && antX >= 0 && antY >= 0) {
            if (plane[antY][antX]) {
                if (xChange == 0) {
                    xChange = yChange;
                    yChange = 0;
                } else {
                    yChange = -xChange;
                    xChange = 0;
                }
            } else {
                if (xChange == 0) {
                    xChange = -yChange;
                    yChange = 0;
                } else {
                    yChange = xChange;
                    xChange = 0;
                }
            }
            plane[antY][antX] = !plane[antY][antX];
            antX += xChange;
            antY += yChange;
        }
        return plane;
    }
}
```