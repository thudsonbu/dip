class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

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
