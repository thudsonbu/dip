const assert = require("assert");

function getLongestNonRepSubstring(s) {
  if (s.length < 2) {
    return s.length;
  }

  let start = 0;
  let record = 0;
  let seenMap = new Map();
  let i = 0;

  while (i < s.length) {
    const char = s[i];

    if (seenMap.has(char) && seenMap.get(char) >= start) {
      start = seenMap.get(char) + 1;
    }

    seenMap.set(char, i);

    record = Math.max(i - start + 1, record);

    i++;
  }

  return record;
}

const cases = [
  { arg: "abba", out: 2 },
  { arg: "a", out: 1 },
  { arg: "aab", out: 2 },
  { arg: "baa", out: 2 },
  { arg: "awwke", out: 3 },
  { arg: "bbbbbb", out: 1 },
  { arg: "abcdabcdea", out: 5 },
  { arg: "abcabcaezccba", out: 5 },
];

for (const { arg, out } of cases) {
  let got;
  try {
    got = getLongestNonRepSubstring(arg);
    assert(got === out);
  } catch (err) {
    console.error(arg, out, got);
  }
}
