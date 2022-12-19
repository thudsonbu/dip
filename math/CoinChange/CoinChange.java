package math.CoinChange;

import java.util.Arrays;
import java.util.Stack;

public class CoinChange {
  public int coinChange(int[] coins, int amount) {
    Arrays.sort(coins);
    Stack<Integer> coinsUsed = new Stack<>();

    int coinIdx = coins.length - 1;
    int coinVal = coins[coinIdx];

    while (amount > 0) {
      while (amount > coinVal) {
        amount -= coinVal;
        coinsUsed.push(coinVal);
      }

      coinIdx--;
      coinVal
    }

    return coinCount;
  }

  public void 
}
