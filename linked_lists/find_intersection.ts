class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function getIntersectionNode(
  headA: ListNode | null,
  headB: ListNode | null
): ListNode | null {
  const seen = new Set<ListNode>();

  while (headA) {
    seen.add(headA);
    headA = headA.next;
  }

  while (headB) {
    if (seen.has(headB)) {
      return headB;
    }
    headB = headB.next;
  }

  return null;
}
