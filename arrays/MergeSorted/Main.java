package MergeSorted;

public class Main {
  public static void main(String args[]) {
    int[] arr1 = { -1, 2, 3, 0, 0, 0, 0 };
    int[] arr2 = { 1, 3, 4, 5 };

    MergeSorted merger = new MergeSorted();

    merger.merge(arr1, 3, arr2, 4);

    for (int num : arr1) {
      System.out.println(num);
    }

    int[] arr3 = { 1 };
    int[] arr4 = {};

    merger.merge(arr3, 1, arr4, 0);

    for (int num : arr3) {
      System.out.println(num);
    }
  }
}
