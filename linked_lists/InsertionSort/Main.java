package linked_lists.InsertionSort;

public class Main {
  public static void main(String args[]) {
    ListNode first = new ListNode(0);
    ListNode second = new ListNode(1);
    ListNode fourth = new ListNode(5);
    ListNode third = new ListNode(2);

    fourth.next = first;
    first.next = third;
    third.next = second;

    InsertionSort sorter = new InsertionSort();

    ListNode result = sorter.insertionSortListV2(fourth);

    while (result != null) {
      System.out.println(result.val);
      result = result.next;
    }
  }
}
