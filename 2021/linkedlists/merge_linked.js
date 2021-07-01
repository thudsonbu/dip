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
	let index;

	// find the base list to merge into (will be list with smallest start val)
	for ( i = 0; i < lists.length; i++ ) {
		if ( lists[i].val < min ) {
			baselist = i;
			min = lists[i].val;
		}
	}

	// remove base list
	lists.slice( baseList, 1 );

	// insert next min if less then base list ref next
	while ( lists.legth ) {
		index = 	

	}

	// ref of snipped list = next if next else remove from array
}