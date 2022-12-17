package linked_lists.InsertionSort;

public class InsertionSort {
  public ListNode insertionSortListV2(ListNode head) {
    if (head.next == null) {
      return head;
    }

    // Prepend a node so that we can add items before the start of the existing
    // list.
    ListNode prepend = new ListNode(0);

    // Current node we are comparing against as we iterate from start to end
    ListNode comparator = head;
    // Node just before we are comparing against. We will set the the `next`
    // value to the node that is being moved when we insert it.
    ListNode previous = prepend;

    // Node that we will try to move.
    ListNode moving = head;

    // Start a loop for going through each item that should be moved.
    while (moving != null) {
      // Find the first node in the list that is larger then the node we are
      // inserting.
      while (comparator.val < moving.val) {
        previous = comparator;
        comparator = comparator.next;

        // If the comparator is null we have reached the end of the list so
        // break.
        if (comparator == null) {
          break;
        }
      }

      // Splice in the moving node by adding it as the next node to the
      // previous.
      ListNode store = moving.next;
      moving.next = previous.next;
      previous.next = moving;
      moving = store;

      // Reset comparator and previous to start of list.
      comparator = prepend.next;
      previous = prepend;

      // How do we ensure that the last item in the list doesn't link to
      // anything?

      // Answer:
    }

    return prepend.next;
  }
}
