package MergeSorted;

public class MergeSorted {
  public void merge(int[] nums1, int m, int[] nums2, int n) {
    int[] nums1Copy = new int[m];

    System.arraycopy(nums1, 0, nums1Copy, 0, m);

    int nums1Index = 0;
    int nums2Index = 0;
    int i = 0;

    while (nums1Index < m && nums2Index < n) {
      int nums1Num = nums1Copy[nums1Index];
      int nums2Num = nums2[nums2Index];

      if (nums1Num <= nums2Num) {
        nums1[i] = nums1Num;
        nums1Index++;
      } else {
        nums1[i] = nums2Num;
        nums2Index++;
      }

      i++;
    }

    if (nums1Index < m) {
      System.arraycopy(nums1Copy, nums1Index, nums1, i, m - nums1Index);
    }

    if (nums2Index < n) {
      System.arraycopy(nums2, nums2Index, nums1, i, n - nums2Index);
    }
  }
}
