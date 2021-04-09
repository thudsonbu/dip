//Given a sorted array nums, remove the duplicates in-place such that each
// element appears only once and returns the new length.

// Do not allocate extra space for another array, you must do this by modifying
// the input array in-place with O(1) extra memory.

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
  let len = nums.length;
  let index = 1;

  if ( len === 1 ) return 1;

  while (true) {
    if ( nums[index] === nums[index-1] ) {
      nums.splice(index-1, 1);
      len -= 1;
    } else {
      index++;
    }

    if ( index >= len ) {
      break;
    }
  }

  return len;
};

let arr = [0,0,1,1,1,2,2,3,3,4];

console.log( removeDuplicates( arr ) );
