import javax.swing
import java.awt

class OutputSwing:
    def main(args):
        SwingUtilities.invokeLater(Runnable(){
            def run():
                JOptionPane.showMessageDialog(None, "Goodbye, World!")  # in alert box
                frame = JFrame("Goodbye, World!")            # on title bar
                text = JTextArea("Goodbye, World!")       # in editable area
                button = JButton("Goodbye, World!")         # on button

                frame.setLayout(FlowLayout())
                frame.add(button)
                frame.add(text)
                frame.pack()
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
                frame.setVisible(True)