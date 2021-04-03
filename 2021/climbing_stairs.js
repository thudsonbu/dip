// On a staircase, the i-th step has some non-negative cost cost[i] assigned 
// (0 indexed).

// Once you pay the cost, you can either climb one or two steps. You need to 
// find minimum cost to reach the top of the floor, and you can either start 
// from the step with index 0, or the step with index 1.

/**
 * @param {number[]} cost
 * @return {number}
 */
var minCostClimbingStairs = function(cost) {
  let first = helper(0, cost);
  let second = helper(1, cost);

  if ( first < second ) {
    return first;
  } else {
    return second;
  }
};

function helper(index, cost) {
  let next = 0;
  let hop = 0;

  if (index+1 < cost.length) {
    next = helper(index+1, cost);
  }

  if (index+2 < cost.length) {
    hop = helper(index+2, cost);
  }

  if ( next < hop ) {
    return cost[index] + next;
  } else {
    return cost[index] + hop;
  }
}

let arr = [1,0,10,11,13]

console.log(minCostClimbingStairs(arr));