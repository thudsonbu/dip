package ThreeSum;

import java.util.List;

public class Main {
  public static void main(String[] args) {
    int[] nums = {-1,0,1,2,-1,-4};

    List<List<Integer>> res = ThreeSum.threeSum(nums);

    for (List<Integer> triplet : res) {
      System.out.println(triplet);
    }
  }
}
