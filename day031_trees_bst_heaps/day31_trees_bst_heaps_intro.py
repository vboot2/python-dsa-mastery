"""
Day 31: Trees, BST, Heaps

BST validation and common tree operations:
- Validate BST - inorder traversal with checks
- Kth Smallest Element in BST - inorder traversal to collect nodes
- Lowest Common Ancestor - recursion on left/right subtrees
"""

# -------------------------------
# Example 1: Validate Binary Search Tree
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    """
    Check inorder traversal produces strictly increasing values.
    """
    prev = [None]

    def inorder(node):
        if not node:
            return True
        if not inorder(node.left):
            return False
        if prev[0] is not None and node.val <= prev[0]:
            return False
        prev[0] = node.val
        return inorder(node.right)

    return inorder(root)

tree = TreeNode(2, TreeNode(1), TreeNode(3))
print("Valid BST?", is_valid_bst(tree))


# -------------------------------
# Example 2: Kth Smallest in BST
# -------------------------------
def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Use inorder traversal to find kth element.
    """
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print("Kth Smallest (k=1):", kth_smallest(tree, 1))


# -------------------------------
# Example 3: Lowest Common Ancestor of Binary Tree
# -------------------------------
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Recursively search for p and q in left and right subtrees.
    """
    if not root or root == p or root == q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right

p = TreeNode(5)
q = TreeNode(1)
root = TreeNode(3, p, q)
lca = lowest_common_ancestor(root, p, q)
print("LCA of 5 and 1:", lca.val)
