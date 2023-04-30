function curry(fn: Function): Function {
  const necessaryArgCount = fn.length;
  const accumulatedArgs = [];
  return function curried(...args) {
    accumulatedArgs.push(...args);
    if (accumulatedArgs.length === necessaryArgCount) {
      return fn(...accumulatedArgs);
    } else {
      return curried;
    }
  };
}

function example(a: string, b: string) {
  return a + " " + b;
}

const curried = curry(example);
const curried2 = curry(example);

console.log(curried("a")("b"));
console.log(curried2("a", "b"));
