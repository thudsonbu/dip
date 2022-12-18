package SubarraySum;

public class Main {

  public static void main(String args[]) {
    SubarraySum summer = new SubarraySum();

    int[] nums = { 1, 1, 1 };

    int result = summer.brainSubarraySum(nums, 2);

    assert( result == 2 );
  }
}
