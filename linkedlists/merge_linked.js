// You are given an array of k linked-lists lists, each linked-list is sorted 
// in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

class Link {
	constructor( val, next ) {
		this.val = val;
		this.next = next;
	}
}

function mergeArrOfLists( lists ) {
	let pairs = [];
	
	while ( lists.length > 1 ) {

		while ( lists.length ) {
			if ( lists.length > 1 ) {
				pairs.push( lists.splice( 0, 2 ) );
			} else {
				pairs.push( lists.splice( 0, 1 ) );
			}
		}

		pairs.forEach( pair => {
			if ( pair.length > 1 ) {
				lists.push( mergeTwoLists( pair[0], pair[1] ) );
			} else {
				lists.push( pair[0] );
			}
		});

		pairs = [];
	}

	return lists[0];
}

function mergeTwoLists( list1, list2 ) {
	let baseList;
	let mergeList;
	let head;

	if ( list1.val < list2.val ) {
		baseList = list1;
		mergeList = list2;
	} else {
		baseList = list2;
		mergeList = list1;
	}

	head = baseList;

	while ( mergeList ) {

		if ( !head.next ) {
			head.next = mergeList;

			break;

		} else if ( mergeList.val < head.next.val ) {

			let tmpNext = head.next;
			head.next = new Link( mergeList.val, tmpNext );

			mergeList = mergeList.next || null;
		}

		head = head.next || null;
	}

	return baseList;
}

function printList( list ) {
	while ( list ) {
		console.log( list.val );
		list = list.next || null;
	}
}

const ll1 = new Link( 1, new Link( 3, null ) );
const ll2 = new Link( 2, null );
const ll3 = new Link( 3, new Link( 6, null ) );
const ll4 = new Link( 0, null );
const ll5 = new Link( 4, new Link( 5, null) );

printList( mergeArrOfLists( [ ll1, ll2, ll3, ll4, ll5 ] ) );