package maps.UniqueOccurrences;

public class Main {
  public static void main(String args[]) {
    int[] uniqueArr = { 1, 2, 2, 3, 3, 3 };
    int[] badArr = { 1, 2, 3, 3 };

    boolean good = UniqueOccurrences.uniqueOccurrences(uniqueArr);
    boolean bad = UniqueOccurrences.uniqueOccurrences(badArr);

    System.out.println("good: " + good);
    System.out.println("bad: " + bad);
  }
}
