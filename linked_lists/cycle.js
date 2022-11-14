// Given the head of a linked list, return the node where the cycle begins. If
// there is no cycle, return null.

// Using hash set
function detectCycle(head) {
  if (!head || !head?.next) {
    return null;
  }

  let ref = head;

  // Set of seen pointers
  const seen = new Set();

  for (let i = 0; i < 10000; i++) {
    if (seen.has(ref)) {
      return ref;
    }

    seen.add(ref);

    if (!ref.next) {
      return null;
    }

    ref = ref.next;
  }

  return null;
}
