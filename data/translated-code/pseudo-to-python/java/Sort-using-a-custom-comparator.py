import java.util.Comparator
import java.util.Arrays

class Test:
  def main():
    strings = ["Here", "are", "some", "sample", "strings", "to", "be", "sorted"]

    Arrays.sort(strings, Comparator {
      def compare(s1, s2):
        c = len(s2) - len(s1)
        if c == 0:
          c = ord(s1.lower()) - ord(s2.lower())
        return c
    })

    for s in strings:
      print(s + " ")