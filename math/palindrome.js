const assert = require("assert");

/**
 * Check if a number is a palindrome
 * @param {number} x
 * @return {boolean}
 */
function isPalindrome(x) {
  if (x < 0 || x === 10) {
    return false;
  }

  if (x < 10) {
    return true;
  }

  let magnitude = 1;
  while (true) {
    const negated = x - magnitude;

    if (negated < 0) {
      break;
    }

    magnitude *= 10;
  }

  // use two pointers, one at each end of the x
  let lowMag = 10;
  let highMag = magnitude / 10;

  while (lowMag < highMag) {
    // covert pointers corresponding digits to the same magnitude
    let lowDig = (x % lowMag) / (lowMag / 10);
    let highDig = Math.floor(x / highMag);

    // subtract them from each other, if difference not palindrome
    const diff = lowDig - highDig;

    if (diff) {
      return false;
    }

    // subtract digits multiplied by magnitude from x (removing them)
    x -= highDig * highMag + lowDig * (lowMag / 10);

    // move pointers inward
    lowMag *= 10;
    highMag /= 10;
  }

  return true;
}

const cases = [
  { val: 121, out: true },
  { val: -121, out: false },
  { val: 1111, out: true },
  { val: 1, out: true },
  { val: 100, out: false },
  { val: 200, out: false },
  { val: 10, out: false },
  { val: 44445, out: false },
  { val: 34543, out: true },
  { val: 111111111111111, out: true },
];

for (const { val, out } of cases) {
  try {
    assert(isPalindrome(val) === out);
  } catch (err) {
    console.log(val, out);
  }
}
