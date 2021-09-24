const assert = require('assert');

// Given n non-negative integers a1, a2, ..., an , where each represents a point
// at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
// of the line i is at (i, ai) and (i, 0). Find two lines, which, together with
//the x-axis forms a container, such that the container contains the most water.

function maxArea( heights ) {
  let left = 0;
  let right = heights.length - 1;
  let max = Math.min( heights[ left ], heights[ right ] ) * ( right - left );

  while ( right !== left ) {
    if ( heights[ left ] < heights[ right ] ) {
      left++;

      if ( heights[ left ] > heights[ left - 1 ] ) {
        max = Math.max(
          ( Math.min( heights[ left ], heights[ right ] ) * ( right - left ) ),
          max
        );
      }

    } else {
      right -= 1;

      if ( heights[ right ] > heights[ right + 1 ] ) {
        max = Math.max(
          ( Math.min( heights[ left ], heights[ right ] ) * ( right - left ) ),
          max
        );
      }
    }
  }

  return max;
}


const first = [ 1, 1 ];
assert( maxArea(first) === 1 );

const second = [ 4, 3, 2, 1, 4 ];
assert( maxArea(second) === 16 );

const third = [ 1, 2, 1 ];
assert( maxArea(third) === 2 );
