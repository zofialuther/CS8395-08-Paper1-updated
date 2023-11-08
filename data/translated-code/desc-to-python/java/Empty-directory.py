import java.nio.file.Files;
import java.nio.file.Path;
import java.io.File;

public class DirectoryChecker {
    public static boolean isDirectoryEmpty(String directoryName) {
        Path path = Paths.get(directoryName);
        File file = path.toFile();
        File[] files = file.listFiles();
        if (files.length == 0) {
            return true;
        } else {
            return false;
        }
    }
}