import java.lang.management.ManagementFactory;

public class ProgramName {
    public static void main(String[] args) {
        String command = ManagementFactory.getRuntimeMXBean().getInputArguments().toString();
        String processName = command.split(" ")[0];
        System.out.println("Currently running program: " + processName);
    }
}