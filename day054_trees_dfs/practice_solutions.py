"""
Day 54: Trees + DFS - LeetCode Problem Solutions
"""

from typing import List, Optional


# ---------------------------------------------------------
# Definition for a binary tree node
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ---------------------------------------------------------
# Problem: Path Sum (LeetCode 112, Easy)
# Link: https://leetcode.com/problems/path-sum/
# ---------------------------------------------------------
class SolutionProblemOne:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


# ---------------------------------------------------------
# Problem: Path Sum II (LeetCode 113, Medium)
# Link: https://leetcode.com/problems/path-sum-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(node, path, remaining):
            if not node:
                return
            path.append(node.val)
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                result.append(list(path))
            else:
                dfs(node.left, path, remaining)
                dfs(node.right, path, remaining)
            path.pop()

        dfs(root, [], targetSum)
        return result


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    # Build tree for testing
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)

    print("Problem 112 Example:", SolutionProblemOne().hasPathSum(root, 22))
    print("Problem 113 Example:", SolutionProblemTwo().pathSum(root, 22))
