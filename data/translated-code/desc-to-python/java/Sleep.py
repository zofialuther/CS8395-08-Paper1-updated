import java.util.Scanner;

public class SleepProgram {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter time in milliseconds: ");
        try {
            long time = scanner.nextLong();
            Thread.sleep(time);
            System.out.println("Awake!");
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter a valid time in milliseconds.");
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted while sleeping.");
        }
    }
}