/**
 * @param {number[]} nums
 * @return {number}
 */
function pivotIndex(nums) {
  const sum = nums.reduce((acc, n) => acc + n);

  let leftSum = 0;
  for (let i = 0; i < nums.length; i++) {
    if (leftSum === sum - (leftSum + nums[i])) {
      return i;
    }

    leftSum += nums[i];
  }

  return -1;
}

const cases = [
  { args: [[1, 2, 3]], out: -1 },
  {
    args: [[1, 1, 5, 2, 3, 1]],
    out: -1,
  },
  {
    args: [[5, 5, 2, 2, 1]],
    out: 1,
  },
  {
    args: [[5, 9, 3, 1, 1]],
    out: 1,
  },
  {
    args: [[7, 1, -1]],
    out: 0,
  },
];

for ({ args, out } of cases) {
  const got = pivotIndex(...args);

  console.log(got, "should be", out, "with args", ...args);
}
