"""
Day 29: Trees, BST, Heaps

Binary tree basics:
- Invert Binary Tree - recursive swapping of children
- Diameter of Binary Tree - longest path between two nodes
- Subtree of Another Tree - recursion + tree matching
"""

from typing import Optional

# -------------------------------
# Binary Tree Node
# -------------------------------
class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------------
# Example 1: Invert Binary Tree
# -------------------------------
def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Recursively swap left and right children of all nodes.
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def preorder(root: Optional[TreeNode]):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []


# Build simple tree:    4
#                      / \
#                     2   7
root = TreeNode(4, TreeNode(2), TreeNode(7))
print("Preorder before invert:", preorder(root))
root = invert_tree(root)
print("Preorder after invert:", preorder(root))


# -------------------------------
# Example 2: Diameter of Binary Tree
# -------------------------------
def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    """
    Diameter = longest path between two nodes
    Use DFS to compute height + update max diameter
    """
    diameter = 0

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter = max(diameter, left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print("Diameter of tree:", diameter_of_binary_tree(root))


# -------------------------------
# Example 3: Subtree of Another Tree
# -------------------------------
def is_same_tree(s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and is_same_tree(s.left, t.left) and is_same_tree(s.right, t.right)


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Check if subRoot is a subtree of root.
    """
    if not root:
        return False
    if is_same_tree(root, subRoot):
        return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


tree = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
sub = TreeNode(4, TreeNode(1), TreeNode(2))
print("Is subtree:", is_subtree(tree, sub))
