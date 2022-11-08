const assert = require("assert");

function getMedian(arr) {
  if (arr.length % 2 === 0) {
    return (
      (arr[Math.floor(arr.length / 2) - 1] + arr[Math.floor(arr.length / 2)]) /
      2
    );
  }

  return arr[Math.floor(arr.length / 2)];
}

function solution(nums1, nums2) {
  // get medians
  const median1 = getMedian(nums1);
  const median2 = getMedian(nums2);

  // We know that the new median will be somewhere between the two current
  // medians so everything less then that smaller median can be placed at the
  // beginning of the final array and everything greater then the larger median
  // can be placed at the end of the final array.

  let left =
    median1 < median2
      ? nums1.splice(0, Math.floor(nums1.length / 2) - 1)
      : nums2.splice(0, Math.floor(nums2.length / 2) - 1);

  let right =
    median2 > median1
      ? nums2.splice(
          Math.floor(nums2.length) + 1,
          Math.floor(nums2.length / 2) - 1
        )
      : nums1.splice(
          Math.floor(nums1.length) + 1,
          Math.floor(nums1.length / 2) - 1
        );

  console.log(left, right);

  // Merge sort numbers in between means
  let center = [];
  while (nums1.length && nums2.length) {
    if (nums1[0] < nums2[0]) {
      center.push(nums1.shift());
    } else {
      center.push(nums2.shift());
    }
  }

  // Add remaining elements after one array runs out
  if (nums1.length) {
    center.push(...nums1);
  } else {
    center.push(...nums2);
  }

  return getMedian(left.concat(center, right));
}

const cases = [
  // {
  //   args: [
  //     [1, 2, 3],
  //     [4, 5, 6],
  //   ],
  //   out: 3.5,
  // },
  // {
  //   args: [
  //     [1, 2, 3],
  //     [1, 2, 3],
  //   ],
  //   out: 2,
  // },
  // {
  //   args: [
  //     [1, 2, 3, 4, 5, 6, 7, 8, 9],
  //     [3, 4, 5, 7, 10, 11, 12, 13],
  //   ],
  //   out: 6,
  // },
  // {
  //   args: [
  //     [1, 2, 3, 4, 5, 6, 7, 8, 9],
  //     [3, 4, 5, 7, 7, 10, 11, 12, 13],
  //   ],
  //   out: 6.5,
  // },
  // {
  //   args: [[1, 3], [2]],
  //   out: 2,
  // },
  {
    args: [
      [1, 4],
      [2, 3],
    ],
    out: 2.5,
  },
];

for (const { args, out } of cases) {
  const got = solution(...args);

  try {
    assert(got === out);
  } catch (err) {
    console.log(got, "should be", out);
  }
}
