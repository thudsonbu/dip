// Given an array of integers nums.

// A pair (i,j) is called good if nums[i] == nums[j] and i < j.

// Return the number of good pairs.

/**
 * @param {number[]} nums
 * @return {number}
 */
var numIdenticalPairs = function (nums) {
  let pairs = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i; j < nums.length; j++) {
      if (j == i) continue;

      if (nums[i] == nums[j]) {
        pairs += 1;
      }
    }
  }

  return pairs;
};

let nums = [1, 2, 3, 1, 1, 3];

console.log(numIdenticalPairs(nums));
