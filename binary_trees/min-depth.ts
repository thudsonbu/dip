import { TreeNode } from "./tree_node";

function minDepth(root: TreeNode | null): number {
  if (!root) return 0;

  return traverse(root);
}

function traverse(root: TreeNode): number {
  if (!root.left && !root.right) return 1;

  let min = 0;

  if (root.left) min = traverse(root.left);

  if (root.right && min) {
    min = Math.min(traverse(root.right), min);
  } else if (root.right) {
    min = traverse(root.right);
  }

  return min + 1;
}
