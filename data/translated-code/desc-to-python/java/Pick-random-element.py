import java.util.Random;

public class RandomArray {
    public static void main(String[] args) {
        Random rand = new Random();
        int[] array = {1, 2, 3};
        int randomIndex = rand.nextInt(array.length);
        int randomValue = array[randomIndex];
        System.out.println("Random value from array: " + randomValue);
        // Re-use the Random object for efficiency
    }
}