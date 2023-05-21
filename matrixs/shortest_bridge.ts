/**
 * You are given an n x n binary matrix grid where 1 represents land and 0
 * represents water. An island is a 4-directionally connected group of 1's not
 * connected to any other 1's. There are exactly two islands in the grid. You
 * may change 0's to 1's to connect the two islands to form one island. Return
 * the smallest number of 0's you must flip to connect the two islands.
 *
 * Input: grid = [
 *  [0,1],
 *  [1,0]
 * ]
 * Output: 1
 *
 * Input: grid = [
 *  [0,1,0],
 *  [0,0,0],
 *  [0,0,1]
 * ]
 * Output: 2
 *
 * Input: grid = [
 *  [1,1,1,1,1],
 *  [1,0,0,0,1],
 *  [1,0,1,0,1],
 *  [1,0,0,0,1],
 *  [1,1,1,1,1]
 * ]
 * Output: 1
 */

function shortestBridge(grid: number[][]): number {
  let queue: [number, number][] = [];
  let found = false;
  let steps = 0;

  // Find the first island
  for (let i = 0; i < grid.length; i++) {
    if (found) break;
    for (let j = 0; j < grid[i].length; j++) {
      if (grid[i][j] === 1) {
        dfs(grid, i, j, queue);
        found = true;
        break;
      }
    }
  }
}
