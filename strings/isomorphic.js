function solution(s, t) {
  if (s.length !== t.length) {
    return false;
  }

  const sMap = new Map();
  const tMap = new Map();

  for (let i = 0; i < s.length; i++) {
    if (sMap.has(s[i]) && sMap.get(s[i]) !== t[i]) {
      return false;
    }

    if (tMap.has(t[i]) && tMap.get(t[i]) !== s[i]) {
      return false;
    }

    sMap.set(s[i], t[i]);
    tMap.set(t[i], s[i]);
  }

  return true;
}

const cases = [
  { args: ["aba", "cbc"], out: true },
  { args: ["egg", "add"], out: true },
  { args: ["ebe", "err"], out: false },
  { args: ["paper", "title"], out: true },
  { args: ["badc", "baba"], out: false },
];

for (const c of cases) {
  const out = solution(...c.args);
  console.log(out, "should be", c.out, "for args", ...c.args);
}
