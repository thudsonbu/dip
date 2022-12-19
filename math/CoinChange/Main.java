package math.CoinChange;

public class Main {
  public static void main(String args[]) {
    CoinChange cc = new CoinChange();

    int[][][] tests = {
        {
            { 5, 1 },
            { 10 },
            { 2 },
        },
        {
            { 1, 2, 5 },
            { 11 },
            { 3 },
        },
        {
            { 5 },
            { 1 },
            { -1 }
        },
        {
            { 10, 5, 1 },
            { 17 },
            { 4 }
        },
    };

    for (int[][] test : tests) {
      int[] coins = test[0];
      int[] amount = test[1];
      int[] expected = test[2];

      int output = cc.coinChange(coins, amount[0]);

      if (output != expected[0]) {
        throw new Error("output: " + output + " should be expected: " + expected[0]);
      }
    }
  }
}
