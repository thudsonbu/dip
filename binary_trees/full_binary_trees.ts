import { TreeNode } from "./tree_node";

function allPossibleFBT(n: number): Array<TreeNode | null> {
  if (n % 2 === 0) return [];
  const treeMemo = new Map<number, Array<TreeNode | null>>();
  treeMemo.set(1, [new TreeNode(0)]);
  treeMemo.set(0, []);
  return allPossibleFBTHelper(n, treeMemo);
}

function allPossibleFBTHelper(
  n: number,
  treeMemo: Map<number, Array<TreeNode | null>>
): Array<TreeNode | null> {
  if (treeMemo.has(n)) return treeMemo.get(n);
  const result: Array<TreeNode | null> = [];
  for (let i = 1; i < n; i += 2) {
    const left = allPossibleFBTHelper(i, treeMemo);
    const right = allPossibleFBTHelper(n - i - 1, treeMemo);
    for (const l of left) {
      for (const r of right) {
        const root = new TreeNode(0);
        root.left = l;
        root.right = r;
        result.push(root);
      }
    }
  }
  treeMemo.set(n, result);
  return result;
}

function main() {
  const result0 = allPossibleFBT(0);
  console.log("Result 0", JSON.stringify(result0, null, 2));
  const result3 = allPossibleFBT(3);
  console.log("Result 3", JSON.stringify(result3, null, 2));
  const result5 = allPossibleFBT(5);
  console.log("Result 5", JSON.stringify(result5, null, 2));
}

main();
