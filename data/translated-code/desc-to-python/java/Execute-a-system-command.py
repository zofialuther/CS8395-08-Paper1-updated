import java.io.IOException;
import java.io.InputStream;

public class ExecuteCommand {
    public static void main(String[] args) {
        executeCmd("ls -oa");
    }

    public static void executeCmd(String command) {
        try {
            Process process = Runtime.getRuntime().exec(command);
            process.waitFor();
            InputStream inputStream = process.getInputStream();
            int i;
            while ((i = inputStream.read()) != -1) {
                System.out.print((char) i);
            }
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}