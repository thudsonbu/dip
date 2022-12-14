package ThreeSum;

import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class ThreeSum {
  /**
   * Given an integer array nums, return all the triplets [nums[i], nums[j],
   * nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] +
   * nums[k] == 0.
   */
  public static List<List<Integer>> threeSum(int[] nums) {
    // 1 find all unique combinations of two numbers and store them in a map
    // from sum to index pair
    HashMap<Integer, List<int[]>> sumToIdxMap = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
      for (int j = i + 1; j < nums.length; j++) {
        int sum = nums[i] + nums[j];

        List<int[]> list = sumToIdxMap.get(sum);

        if (list == null) {
          list = new ArrayList<>();
          sumToIdxMap.put(sum, list);
        }

        list.add(new int[] { j, i });
      }
    }

    // For each number, check if the map contains a key that is the negative of
    // the number. If so, add the number and the two numbers that sum to the
    // negative of the number to the result. Use a set to avoid duplicates.

    List<List<Integer>> result = new ArrayList<>();
    HashSet<List<Integer>> seen = new HashSet<>();

    for (int i = 0; i < nums.length; i++) {
      int num = nums[i];
      List<int[]> list = sumToIdxMap.get(-num);

      if (list != null) {
        for (int[] idxPair : list) {
          int idx1 = idxPair[0];
          int idx2 = idxPair[1];

          if (idx1 != i && idx2 != i) {
            List<Integer> triplet = new ArrayList<>();

            triplet.add(nums[idx1]);
            triplet.add(nums[idx2]);
            triplet.add(num);

            triplet.sort((a, b) -> a - b);

            if (!seen.contains(triplet)) {
              result.add(triplet);
              seen.add(triplet);
            }
          }
        }
      }
    }

    return result;
  }
}
