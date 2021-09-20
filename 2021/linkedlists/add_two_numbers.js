
function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val);
  this.next = (next===undefined ? null : next);

  return this;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let carry = 0;
  let list;
  let sum;

  while ( l1.next || l2.next ) {
    sum = l1.val + l2.val + carry;

    console.log( 'iteration' );
    console.log( l1 );

    if ( sum >= 10 ) {
      sum = sum - 10;
      carry = 1;
    } else {
      carry = 0;
    }

    console.log( l1 );

    if ( list ) {
      list.next = ListNode( sum, undefined );
      list = list.next;
    } else {
      list = ListNode( sum, undefined );
    }

    console.log( l1 );

    l1 = l1.next ? l1.next : { val: 0 };
    l2 = l2.next ? l2.next : { val: 0 };
  }

  return list;
};

const l1 = ListNode( 1, undefined )
const l2 = ListNode( 5, l1 );
const l3 = ListNode( 3, l2 );

const l4 = ListNode( 6, undefined );
const l5 = ListNode( 1, l4 );

const list = addTwoNumbers( l3, l5 );

while ( list.next ) {
  console.log( list.val );

  list = list.next;
}
