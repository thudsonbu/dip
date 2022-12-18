package SongCombinations;

import java.util.HashMap;

// You are given a list of songs where the ith song has a duration of time[i]
// seconds.

// Return the number of pairs of songs for which their total duration in seconds
// is divisible by 60. Formally, we want the number of indices i, j such that
// i < j with (time[i] + time[j]) % 60 == 0.

public class SongCombinations {
  public int numPairsDivisibleBy60(int[] time) {
    // First get remainder of each element when dividing by sixty and replace in
    // array.
    HashMap<Integer, Integer> countMap = new HashMap<>();

    for (int i = 0; i < time.length; i++) {
      int remainder = time[i] % 60;

      if (!countMap.containsKey(remainder)) {

        countMap.put(remainder, 1);
      } else {
        int oldCount = countMap.get(remainder);

        countMap.put(remainder, oldCount + 1);
      }
    }

    int count = 0;

    int sixtiesCount = countMap.getOrDefault(0, 0);
    count += this.getFactorial(sixtiesCount);

    int thirtiesCount = countMap.getOrDefault(30, 0);
    count += this.getFactorial(thirtiesCount);

    int low = 1;
    int high = 59;

    while (low != high) {
      int lowCount = countMap.getOrDefault(low, 0);
      int highCount = countMap.getOrDefault(high, 0);

      count += lowCount * highCount;

      low += 1;
      high -= 1;
    }

    return count;
  }

  public int getFactorial(int num) {
    if (num == 0) {
      return num;
    }

    int fact = 0;

    for (int i = 1; i < num; i++) {
      fact += i;
    }

    return fact;
  }
}
