```python
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class DerangedAnagrams {
    public static void main(String[] args) {
        List<String> words = new ArrayList<>();
        try {
            words = Files.readAllLines(new File("unixdict.txt").toPath());
        } catch (IOException e) {
            e.printStackTrace();
        }
        printLongestDerangedAnagram(words);
    }

    private static void printLongestDerangedAnagram(List<String> words) {
        words.sort((s1, s2) -> {
            if (s1.length() != s2.length()) {
                return s2.length() - s1.length();
            } else {
                return s1.compareTo(s2);
            }
        });
        Map<String, List<String>> map = new HashMap<>();
        for (String word : words) {
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String key = new String(charArray);
            map.putIfAbsent(key, new ArrayList<>());
            List<String> anagrams = map.get(key);
            for (String anagram : anagrams) {
                if (isDeranged(anagram, word)) {
                    System.out.println(anagram + " " + word);
                    return;
                }
            }
            anagrams.add(word);
        }
        System.out.println("no result");
    }

    private static boolean isDeranged(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        for (int i = 0; i < word1.length(); i++) {
            if (word1.charAt(i) == word2.charAt(i)) {
                return false;
            }
        }
        return true;
    }
}
```