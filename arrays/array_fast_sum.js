const { assert } = require('chai');

/**
 * Create a class that initializes with a list of numbers and has one method
 * called sum. sum should take in two parameters, start_idx and end_idx and
 * return the sum of the list from start_idx (inclusive) to end_idx`
 * (exclusive). You should optimize for the sum method.
 */

class ArrFastSum {
  constructor( arr ) {
    this.arr = arr;

    this.computeRunningSum();
  }

  computeRunningSum() {
    this.runningSum = [ 0 ];

    let sum = 0;
    this.arr.forEach( num => {
      sum = sum + num;
      this.runningSum.push( sum );
    });
  }

  sum( startIndex, endIndex ) {
    return this.runningSum[ endIndex ] - this.runningSum[ startIndex ];
  }
}

const arr = [ 1, 2, 3, 4, 5, 6, 7 ];

const optSum = new ArrFastSum( arr );

assert.strictEqual( optSum.sum( 2, 5 ), 12 );
assert.strictEqual( optSum.sum( 0, 0 ), 0 );
assert.strictEqual( optSum.sum( 0, 7 ), 28 );
