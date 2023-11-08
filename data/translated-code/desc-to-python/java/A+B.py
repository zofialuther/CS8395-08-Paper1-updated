import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.StreamTokenizer;

public class AplusB {
    public static void main(String[] args) {
        try {
            StreamTokenizer tokenizer = new StreamTokenizer(new InputStreamReader(System.in));
            int a = (int) tokenizer.nval;
            tokenizer.nextToken();
            int b = (int) tokenizer.nval;

            int sum = a + b;

            OutputStreamWriter writer = new OutputStreamWriter(System.out);
            writer.write("The sum is: " + sum);
            writer.flush();
        } catch (IOException e) {
            System.out.println("An error occurred during input/output operations.");
        }
    }
}