// You are given two non-empty linked lists representing two non-negative 
// integers. The digits are stored in reverse order, and each of their nodes
// contains a single digit. Add the two numbers and return the sum as a linked 
// list.

// You may assume the two numbers do not contain any leading zero, except the
// number 0 itself.

class Link {
	constructor( val, next ) {
		this.val = val;
		this.next = next;
	}
}

function addTwoNumbers( l1, l2 ) {
	let magnitude = 1;
	let sum = 0;

	while ( l1 && l2 ) {
		sum += ( l1.val + l2.val ) * magnitude;

		l1 = l1.next;
		l2 = l2.next;

		magnitude = magnitude * 10;
	}

	let lastList = l1 || l2 || false;

	while ( lastList ) {
		sum += ( lastList.val ) * magnitude;

		lastList = lastList.next;

		magnitude = magnitude * 10;
	}

	return sum;
}

const testList1 = new Link( 1, new Link( 1, new Link( 1, null ) ) );
const testList2 = new Link( 1, new Link( 1, new Link( 1, null ) ) );

console.assert( addTwoNumbers( testList1, testList2 ) === 222 );

const testList3 = new Link( 5, new Link( 3, new Link( 1, null ) ) );
const testList4 = new Link( 6, new Link( 9, null ) );

console.assert( addTwoNumbers( testList3, testList4 ) === 231 );

const testList5 = new Link( 5, new Link( 3, new Link( 1, null ) ) );
const testList6 = new Link( 0, null );

console.assert( addTwoNumbers( testList5, testList6 ) === 135 );

const testList7 = new Link( 5, new Link( 0, new Link( 1, null ) ) );
const testList8 = new Link( 0, new Link( 5, new Link( 3, new Link( 5, null ) ) ) );

console.assert( addTwoNumbers( testList7, testList8 ) === 5455 );