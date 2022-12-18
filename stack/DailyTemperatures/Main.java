package DailyTemperatures;

public class Main {
  public static void main(String args[]) {
    DailyTemperatures dt = new DailyTemperatures();

    int[][][] tests = {
      {
        { 73, 74, 75, 71, 69, 72, 76, 73 },
        { 1, 1, 4, 2, 1, 1, 0, 0 }
      },
      {
        { 30, 40, 50, 60 },
        { 1, 1, 1, 0 }
      },
      {
        { 30, 60, 90 },
        { 1, 1, 0 }
      }
    };

    for (int[][] test : tests) {
      int[] input = test[0];
      int[] expected = test[1];

      int[] output = dt.dailyTemperatures(input);

      assert (output.equals(expected));
    }
  }
}
