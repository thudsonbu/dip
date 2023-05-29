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

function getIntersectionNode2(
  headA: ListNode | null,
  headB: ListNode | null
): ListNode | null {
  let p1 = headA;
  let p2 = headB;

  while (p1 !== p2) {
    if (p1) {
      p1 = p1.next;
    } else {
      p1 = headB;
    }

    if (p2) {
      p2 = p2.next;
    } else {
      p2 = headA;
    }
  }

  return p1;
}
