function asteroidCollision(asteroids: number[]): number[] {
  if (asteroids.length < 2) {
    return asteroids;
  }
  let leftStack = [asteroids.shift()];
  let rightStack = asteroids;
  while (rightStack.length) {
    if (
      !leftStack.length ||
      leftStack[leftStack.length - 1] < 0 ||
      rightStack[0] > 0
    ) {
      leftStack.push(rightStack.shift());
      continue;
    }
    const diff = leftStack[leftStack.length - 1] + rightStack[0];
    if (diff === 0) {
      leftStack.pop();
      rightStack.shift();
    } else if (diff > 0) {
      rightStack.shift();
    } else {
      leftStack.pop();
    }
  }
  return leftStack;
}

console.log(asteroidCollision([-1, 4, -2, 1, -5]));
console.log(asteroidCollision([8, -8]));
console.log(asteroidCollision([8]));
