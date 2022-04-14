const { assert } = require('chai');

/**
 * Given a sorted list of size n, with m unique elements (thus m < n), modify
 * the list such that the first m unique elements in the list will be sorted,
 * ignoring the rest of the list. Your solution should have a space complexity
 * of O(1). Instead of returning the list (since you are just modifying the
 * original list), you should return what m is.
 */

function countUniqueElements( array ) {
  let i = 0;
  let j = 1;

  while ( j < array.length ) {
    if ( array[ i ] === array[ j ] ) {
      array.splice( j, 1 );
    } else {
      i = j;
      j++;
    }
  }

  return array.length;
}

const arr = [ 1, 1, 2, 5, 6, 7, 7, 7, 8 ];

assert.strictEqual( countUniqueElements( arr ), 6 );
