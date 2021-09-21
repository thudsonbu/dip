class ListNode {
  constructor( val, next ) {
    this.val = val;
    this.next = next;
  }
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
function addTwoNumbers( l1, l2 ) {
  let ref;
  let head;
  let sum = 0;
  let carry = 0;

  while ( l1 && l2 ) {
    sum = l1.val + l2.val + carry;

    if ( sum > 9 ) {
      sum -= 10;
      carry = 1;
    } else {
      carry = 0;
    }

    if ( ref ) {
      ref.next = new ListNode( sum, undefined );
      ref = ref.next;
    } else {
      ref = new ListNode( sum, undefined );
      head = ref;
    }

    l1 = l1.next ? l1.next : undefined;
    l2 = l2.next ? l2.next : undefined;
  }

  if ( l1 ) {
    ref.next = new ListNode( l1.val + carry, l1.next );
  }

  if ( l2 ) {
    ref.next = new ListNode( l2.val + carry, l2.next );
  }

  return head;
};

const l1 = new ListNode( 1, new ListNode( 2, new ListNode( 5, undefined ) ) );
const l2 = new ListNode( 3, new ListNode( 9, undefined ) );

console.log( addTwoNumbers( l1, l2 ) );

const l3 = new ListNode( 1, new ListNode( 2, new ListNode( 5, undefined ) ) );
const l4 = new ListNode( 3, undefined );

console.log( addTwoNumbers( l3, l4 ) );
