// Your country has an infinite number of lakes. Initially, all the lakes are
// empty, but when it rains over the nth lake, the nth lake becomes full of
// water. If it rains over a lake which is full of water, there will be a flood.
// Your goal is to avoid the flood in any lake.

// Given an integer array rains where:

// rains[i] > 0 means there will be rains over the rains[i] lake.
// rains[i] == 0 means there are no rains this day and you can choose one lake
// this day and dry it.
// Return an array ans where:

// ans.length == rains.length
// ans[i] == -1 if rains[i] > 0.
// ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
// If there are multiple valid answers return any of them. If it is impossible
// to avoid flood return an empty array.

/**
 * @param {number[]} rains
 * @return {number[]}
 */
var avoidFlood = function (rains) {
  let ans = [];
  let dryIndexs = [];
  let wetIndexs = [];

  for (let i = 0; i < rains.length; i++) {
    if (rains[i] > 0) {
      ans.push(-1);

      let full = wetIndexs.indexOf(rains[i] - 1);

      if (full >= 0 && dryIndexs.length) {
        ans[dryIndexs.pop()] = wetIndexs[full] + 1;
        wetIndexs.slice(full, full + 1);
      } else if (full >= 0) {
        return [];
      } else {
        wetIndexs.push(rains[i] - 1);
      }
    } else {
      ans.push(-1);
      dryIndexs.unshift(i);
    }
  }

  dryIndexs.forEach((index) => {
    ans[index] = 1;
  });

  return ans;
};

let rains1 = [1, 2, 3, 4];
console.log(avoidFlood(rains1));

let rains2 = [1, 2, 0, 0, 2, 1];
console.log(avoidFlood(rains2));

let rains3 = [1, 2, 0, 1, 1];
console.log(avoidFlood(rains3));

let rains4 = [0, 1, 1];
console.log(avoidFlood(rains4));
