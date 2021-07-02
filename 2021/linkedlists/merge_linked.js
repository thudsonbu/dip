// You are given an array of k linked-lists lists, each linked-list is sorted 
// in ascending order.

// Merge all the linked-lists into one sorted linked-list and return it.

class Link {
	constructor( val, next ) {
		this.val = val;
		this.next = next;
	}
}

// takes an array contained sorted linked lists and merges them
function mergeLinkedLists( lists ) {
	let baseList = 0;
	let min = lists[baseList].val;
	let minListIndex;

	// find the base list to merge into (will be list with smallest start val)
	for ( i = 0; i < lists.length; i++ ) {
		if ( lists[i].val < min ) {
			baseList = i;
			min = lists[i].val;
		}
	}

	// remove base list
	baseList = lists.splice( baseList, 1 );
	out = baseList;

	// while there are still lists to be merged
	while ( lists.length ) {
		let next;

		if ( baseList.next ) {
			next = baseList.next.val;
		} else {
			next = Number.POSITIVE_INFINITY;
		}

		// insert next min if less then base list ref next
		for ( i = 0; i < lists.length; i++ ) {
			if ( lists[i].val < next ) {
				minListIndex = i;
				min = lists[i].val;
			}
		}
		
		// if we find a smaller one insert into ll and set ref to it
		if ( min < next ) {
			let tmp = baseList.next;

			baseList.next = new Link( min, tmp );

			// set ref to next if next in min list else delete
			if ( lists[minListIndex].next ) {
				lists[minListIndex] = lists[minListIndex].next;
			} else {
				lists.splice( minListIndex, 1 );
			}
		}

		baseList = baseList.next || baseList;
	}

	return out;
}

const ll1 = new Link( 1, new Link( 3, null ) );
const ll2 = new Link( 3, null );

console.log( mergeLinkedLists( [ ll1, ll2 ] ) );