```python
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ClickCounter extends JFrame {
    private int clickCount;
    private JLabel clickLabel;

    public ClickCounter() {
        clickCount = 0;
        clickLabel = new JLabel("Click count: " + clickCount);

        JButton clickButton = new JButton("Click me");
        clickButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                clickCount++;
                clickLabel.setText("Click count: " + clickCount);
            }
        });

        setLayout(new BorderLayout());
        add(clickLabel, BorderLayout.NORTH);
        add(clickButton, BorderLayout.CENTER);

        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setTitle("Click Counter");
        setSize(300, 200);
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new ClickCounter();
            }
        });
    }
}
```