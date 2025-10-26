"""
Day 56: BFS + Level Order - LeetCode Problem Solutions
"""

from collections import deque

# ---------------------------------------------------------
# Problem: N-ary Tree Level Order Traversal (LeetCode 429, Medium)
# Link: https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# ---------------------------------------------------------


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children or []


class SolutionProblemOne:
    def solve(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                for child in node.children:
                    queue.append(child)
            res.append(level)
        return res


# ---------------------------------------------------------
# Problem: Find Largest Value in Each Tree Row (LeetCode 515, Medium)
# Link: https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# ---------------------------------------------------------


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionProblemTwo:
    def solve(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_max = float("-inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_max)
        return res


# ---------------------------------------------------------
# Problem: Average of Levels in Binary Tree (LeetCode 637, Easy)
# Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/
# ---------------------------------------------------------


class SolutionProblemThree:
    def solve(self, root):
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level_sum = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum / size)
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------

if __name__ == "__main__":
    # N-ary tree for 429
    root_nary = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
    print("Problem One Example:", SolutionProblemOne().solve(root_nary))

    # Binary tree for 515 and 637
    root_bt = TreeNode(1)
    root_bt.left = TreeNode(3)
    root_bt.right = TreeNode(2)
    root_bt.left.left = TreeNode(5)
    root_bt.left.right = TreeNode(3)
    root_bt.right.right = TreeNode(9)

    print("Problem Two Example:", SolutionProblemTwo().solve(root_bt))
    print("Problem Three Example:", SolutionProblemThree().solve(root_bt))
