```python
import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Timer;
import java.util.TimerTask;

public class RotatingTextApp extends JFrame {
    private JLabel label;
    private Timer timer;
    private int rotationSpeed;

    public RotatingTextApp() {
        label = new JLabel("Hello World!", JLabel.CENTER);
        add(label);

        rotationSpeed = 1;
        timer = new Timer();
        timer.scheduleAtFixedRate(new TimerTask() {
            @Override
            public void run() {
                String text = label.getText();
                label.setText(text.substring(1) + text.charAt(0));
            }
        }, 0, 500);

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (e.getButton() == MouseEvent.BUTTON1) {
                    rotationSpeed = 1;
                } else if (e.getButton() == MouseEvent.BUTTON3) {
                    rotationSpeed = -1;
                }
            }
        });

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(200, 100);
        setVisible(true);
    }

    public static void main(String[] args) {
        new RotatingTextApp();
    }
}
```