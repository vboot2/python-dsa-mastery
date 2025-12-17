"""
Day 29: Trees, BST, Heaps - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Invert Binary Tree (LeetCode 226, Easy)
# Link: https://leetcode.com/problems/invert-binary-tree/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionInvertTree:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# ---------------------------------------------------------
# Problem 2: Diameter of Binary Tree (LeetCode 543, Easy)
# Link: https://leetcode.com/problems/diameter-of-binary-tree/
# ---------------------------------------------------------
class SolutionDiameter:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.diameter


# ---------------------------------------------------------
# Problem 3: Subtree of Another Tree (LeetCode 572, Easy)
# Link: https://leetcode.com/problems/subtree-of-another-tree/
# ---------------------------------------------------------
class SolutionSubtree:
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Test Invert Binary Tree
    root = TreeNode(4, TreeNode(2), TreeNode(7))
    inverted = SolutionInvertTree().invertTree(root)
    print("Invert Tree Root:", inverted.val, "-> Left:", inverted.left.val, "Right:", inverted.right.val)

    # Test Diameter
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Diameter:", SolutionDiameter().diameterOfBinaryTree(root))

    # Test Subtree
    tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    print("Is Subtree:", SolutionSubtree().isSubtree(tree, sub))
