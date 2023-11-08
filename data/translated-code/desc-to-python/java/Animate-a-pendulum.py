```python
import javax.swing.*;
import java.awt.*;

public class Pendulum extends JPanel implements Runnable {
    private double angle;
    private double length;
    private double velocity;
    private double acceleration;

    public void setAngle(double angle) {
        this.angle = angle;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public void paint(Graphics g) {
        // Draw the pendulum using angle and length
    }

    public void run() {
        while (true) {
            // Update the position of the pendulum based on angle, velocity, and acceleration
            // Call repaint to update the display
        }
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Pendulum Animation");
        Pendulum pendulum = new Pendulum();
        frame.add(pendulum);
        Thread thread = new Thread(pendulum);
        thread.start();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setVisible(true);
    }
}
```