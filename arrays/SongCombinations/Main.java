package SongCombinations;

public class Main {
  public static void main(String args[]) {
    SongCombinations comb = new SongCombinations();

    int[] times = { 30, 150, 100, 20, 30, 60, 60 };

    int combCount = comb.numPairsDivisibleBy60(times);

    System.out.println(combCount);
  }
}
