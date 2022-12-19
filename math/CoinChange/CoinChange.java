package math.CoinChange;

import java.util.HashMap;

public class CoinChange {
  public int coinChange(int[] coins, int amount) {
    if (coins.length == 0) {
      return -1;
    }

    if (amount == 0) {
      return 0;
    }

    HashMap<Integer, Integer> amtToCoinCt = new HashMap<>();

    amtToCoinCt.put(0, 0);

    int result = this.changeRecursiveHelper(coins, amount, amtToCoinCt);

    if (result < 0) {
      return -1;
    }

    return result;
  }

  public int changeRecursiveHelper(int[] coins, int amount, HashMap<Integer, Integer> map) {
    if (map.containsKey(amount)) {
      return map.get(amount);
    }

    int minSteps = Integer.MAX_VALUE;

    for (int coin : coins) {
      if (coin > amount)
        continue;

      int coinMin = changeRecursiveHelper(coins, amount - coin, map);

      minSteps = Math.min(coinMin, minSteps);
    }

    map.put(amount, minSteps + 1);

    return minSteps + 1;
  }
}
