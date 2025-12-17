"""
Day 90: Trees  
Trees are hierarchical data structures made of nodes, often used for fast searching, structured representation, and recursion-based algorithms.
"""

# Example 1: Basic Tree Traversal (DFS Preorder)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_one():
    """
    Preorder traversal example: root → left → right
    """
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    result = []

    def preorder(node):
        if not node:
            return
        result.append(node.val)  # visit root
        preorder(node.left)      # traverse left
        preorder(node.right)     # traverse right

    preorder(root)
    return result

print("Output Example 1:", example_one())


# Example 2: BFS Level Order Traversal
from collections import deque

def example_two():
    """
    Level-order traversal using a queue (BFS)
    """
    root = TreeNode(1, TreeNode(2), TreeNode(3))

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result

print("Output Example 2:", example_two())
