"""
Day 32: Trees, BST, Heaps - LeetCode Problem Solutions
"""

from collections import deque

# ---------------------------------------------------------
# Problem 1: Binary Tree Level Order Traversal (LeetCode 102, Medium)
# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/
# ---------------------------------------------------------
class SolutionLevelOrder:
    def levelOrder(self, root):
        if not root:
            return []

        res, q = [], deque([root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res


# ---------------------------------------------------------
# Problem 2: Binary Tree Zigzag Level Order Traversal (LeetCode 103, Medium)
# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# ---------------------------------------------------------
class SolutionZigzagLevelOrder:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res, q, left_to_right = [], deque([root]), True
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if not left_to_right:
                level.reverse()
            res.append(level)
            left_to_right = not left_to_right
        return res


# ---------------------------------------------------------
# Problem 3: Binary Tree Right Side View (LeetCode 199, Medium)
# Link: https://leetcode.com/problems/binary-tree-right-side-view/
# ---------------------------------------------------------
class SolutionRightSideView:
    def rightSideView(self, root):
        if not root:
            return []

        res, q = [], deque([root])
        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == size - 1:  # last node in this level
                    res.append(node.val)
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # Build sample tree: [3,9,20,None,None,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    print("Level Order:", SolutionLevelOrder().levelOrder(root))
    print("Zigzag Level Order:", SolutionZigzagLevelOrder().zigzagLevelOrder(root))
    print("Right Side View:", SolutionRightSideView().rightSideView(root))
