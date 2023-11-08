import javax.swing
import java.awt

class OutputSwing:
    def main(args):
        # Create a new thread to run the Swing GUI
        SwingUtilities.invokeLater(Runnable(){
            def run():
                # Display a message in an alert box
                JOptionPane.showMessageDialog (None, "Goodbye, World!")

                # Create a new JFrame with the title "Goodbye, World!"
                frame = JFrame("Goodbye, World!")

                # Create a new JTextArea with the text "Goodbye, World!"
                text = JTextArea("Goodbye, World!")

                # Create a new JButton with the text "Goodbye, World!"
                button = JButton("Goodbye, World!")

                # Set the layout of the frame to FlowLayout
                frame.setLayout(FlowLayout())

                # Add the button and text area to the frame
                frame.add(button)
                frame.add(text)

                # Adjust the size of the frame to fit its contents
                frame.pack()

                # Set the default close operation for the frame
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)

                # Make the frame visible
                frame.setVisible(True)