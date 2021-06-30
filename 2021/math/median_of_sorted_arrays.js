// Given two sorted arrays nums1 and nums2 of size m and n respectively,
// return the median of the two sorted arrays.

function findMedianSortedArrays( nums1, nums2 ) {
	let total = nums1.length + nums2.length;
	let sorted = [];

	if ( total === 1 ) {
		return nums1[0] || nums2[0];
	}

	// continue till midpoint
	while ( sorted.length <= ( total / 2 ) ) {
		// check that they both still have elements
		if ( nums1.length && nums2.length ) {
			// shift out least element to sorted
			if ( nums1[0] < nums2[0] ) {
				sorted.push( nums1.shift() );
			} else {
				sorted.push( nums2.shift() );
			}
		} else {
			sorted = sorted.concat( nums1, nums2 );
		}
	}

	if ( total % 2 === 0 ) {
		return ( sorted[ total/2 - 1 ] + sorted[ total/2 ] ) / 2;
	} else {
		return sorted[ total/2 + .5 ];
	}
}

let arr1 = [ 1, 2 ];
let arr2 = [ 3, 4 ];

console.assert( findMedianSortedArrays( arr1, arr2 ) === 2.5 );

arr1 = [ 1 ];
arr2 = [ ];

console.assert( findMedianSortedArrays( arr1, arr2 ) === 1 );

arr1 = [ 0, 0 ];
arr2 = [ 0, 0 ];

console.assert( findMedianSortedArrays( arr1, arr2 ) === 0 );

arr1 = [ 1, 2, 3 ];
arr2 = [ 2, 3, 5 ];

console.assert( findMedianSortedArrays( arr1, arr2 ) === 2.5 );

arr1 = [ 1, 2, 2 ];
arr2 = [ 4, 6, 9 ]

console.assert( findMedianSortedArrays( arr1, arr2 ) === 3 );