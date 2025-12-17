"""
Day 32: Trees, BST, Heaps

Level Order Traversals of Binary Trees:
- Standard BFS level-order traversal
- Zigzag level order traversal
- Right side view of the tree
"""

from collections import deque

# -------------------------------
# Example 1: Standard Level Order Traversal (BFS)
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
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

# Build sample tree: [3,9,20,None,None,15,7]
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print("Level Order:", level_order(root))


# -------------------------------
# Example 2: Zigzag Level Order Traversal
# -------------------------------
def zigzag_level_order(root):
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

print("Zigzag Level Order:", zigzag_level_order(root))


# -------------------------------
# Example 3: Right Side View
# -------------------------------
def right_side_view(root):
    if not root:
        return []

    res, q = [], deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == len(q):  # last node in this level
                res.append(node.val)
    return res

print("Right Side View:", right_side_view(root))
