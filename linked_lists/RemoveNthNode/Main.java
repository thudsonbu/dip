package linked_lists.RemoveNthNode;

import java.util.ArrayList;

class Main {
  public ListNode removeNthFromEnd(ListNode head, int n) {
    ArrayList<ListNode> nodes = new ArrayList<>();

    ListNode ref = head;
    nodes.add(ref);

    while (ref.next != null) {
      ref = ref.next;
      nodes.add(ref);
    }

    int cutIndex = nodes.size() - (n + 1);

    if (cutIndex == -1) {
      head = head.next;
    } else {
      ListNode store = nodes.get(cutIndex);

      if (store.next != null) {
        store.next = store.next.next;
      } else {
        store.next = null;
      }
    }

    return head;
  }
}
