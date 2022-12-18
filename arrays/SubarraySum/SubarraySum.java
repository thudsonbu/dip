package SubarraySum;

import java.util.HashMap;

public class SubarraySum {
  public int naiveSubarraySum(int[] nums, int k) {
    // Start from each index in the array and sum from right to left adding
    // a the next element to the right to the previous sum at each step.
    // Increment the k each time that the target is hit.
    int count = 0;

    for (int i = 0; i < nums.length; i++) {
      int sum = 0;

      for (int j = i; j < nums.length; j++) {
        sum += nums[j];

        if (sum == k) {
          count++;
        }
      }
    }

    return count;
  }

  public int brainSubarraySum(int[] nums, int k) {
    int count = 0;
    int sum = 0;

    // Record sum up to the given index in a map from sum to number of times
    // that we have seen the sum.
    HashMap<Integer, Integer> map = new HashMap<>();

    map.put(0, 1);

    for (int i = 0; i < nums.length; i++) {
      sum += nums[i];

      // If there is a sum in the map that has a difference from the current sum
      // of the target value. The sum between those two points is k. Thus
      // we increment the count of sub-arrays found.
      if (map.containsKey(sum - k)) {
        count += map.get(sum - k);
      }

      map.put(sum, map.getOrDefault(sum, 0) + 1);
    }

    return count;
  }
}
