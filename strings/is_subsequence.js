function solution(s, t) {
  let sIndex = 0;

  for (let i = 0; i < t.length; i++) {
    if (t[i] === s[sIndex]) {
      sIndex += 1;
    }
  }

  return s.length === sIndex;
}

const cases = [
  {
    args: ["aba", "acdba"],
    out: true,
  },
  {
    args: ["ccc", "acacac"],
    out: true,
  },
];

for (const c of cases) {
  const out = solution(...c.args);
  console.log(out, "should be", c.out, "for args", ...c.args);
}
