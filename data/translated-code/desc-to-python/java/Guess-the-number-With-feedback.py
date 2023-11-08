import java.util.Scanner;
import java.util.Random;

public class GuessingGame {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Random rand = new Random();
        int randomNumber = rand.nextInt(100) + 1;
        int guess = 0;

        while (guess != randomNumber) {
            System.out.print("Enter your guess: ");
            guess = input.nextInt();
            if (guess < randomNumber) {
                System.out.println("Too low, try again.");
            } else if (guess > randomNumber) {
                System.out.println("Too high, try again.");
            }
        }
        System.out.println("Congratulations! You guessed the correct number.");
    }
}