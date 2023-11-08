import java.util.EnumMap;
import java.util.Map;
import java.util.Random;
import java.util.Scanner;

public class RockPaperScissors {

    enum Choice {
        ROCK, PAPER, SCISSORS
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        Map<Choice, Integer> counts = new EnumMap<>(Choice.class);

        while (true) {
            System.out.print("Enter your choice (rock, paper, scissors) or 'quit' to stop: ");
            String input = scanner.next().toUpperCase();

            if (input.equals("QUIT")) {
                break;
            }

            Choice userChoice = Choice.valueOf(input);
            Choice computerChoice = Choice.values()[random.nextInt(3)];

            System.out.println("Computer chose: " + computerChoice);

            // Compare choices and determine the winner
            // ...

            // Update counts
            counts.put(userChoice, counts.getOrDefault(userChoice, 0) + 1);
        }

        System.out.println("Thanks for playing!");
        System.out.println("Counts: " + counts);
    }
}