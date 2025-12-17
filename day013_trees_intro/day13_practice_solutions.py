"""
Day 13: Practice Solutions
"""

# Definition for a binary tree node.
from queue import Full


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---------------------------------------------------------
# Problem: Maximum Depth of Binary Tree (LeetCode 104)
# Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# ---------------------------------------------------------
class maxDepthSolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ---------------------------------------------------------
# Problem: Same Tree (LeetCode 100)
# Link: https://leetcode.com/problems/same-tree/
# ---------------------------------------------------------
class isSameTreeSolution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        return (p.val == q.val and
                self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))


# ---------------------------------------------------------
# Problem: Symmetric Tree (LeetCode 101)
# Link: https://leetcode.com/problems/symmetric-tree/
# ---------------------------------------------------------
class isSymmetricSolution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val and
                    isMirror(t1.left, t2.right) and
                    isMirror(t1.right, t2.left))
        return isMirror(root, root)

# ------------------------------------------------------
# Example Usage
# ------------------------------------------------------
if __name__ == "__main__":
    # Tree: [1,2,2,3,4,4,3]
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right = TreeNode(2, TreeNode(4), TreeNode(3))

    print("Max Depth:", maxDepthSolution().maxDepth(root))          # Expected 3
    print("Is Same Tree:", isSameTreeSolution().isSameTree(root, root))  # Expected True
    print("Is Symmetric:", isSymmetricSolution().isSymmetric(root))    # Expected True
