"""
Day 92: Trees

Constructing trees, recursive traversals, and nested tree-like structures.
"""

# Example 1: Build BST from sorted array (core idea of LC108)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_one():
    """
    Construct a height-balanced BST from a sorted array
    - Pick middle element as root
    - Recursively build left and right subtrees
    """
    nums = [-10, -3, 0, 5, 9]

    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node

    root = build(0, len(nums) - 1)
    return root.val  # return root value for demonstration

print("Output Example 1:", example_one())


# Example 2: Postorder traversal demonstration
def example_two():
    """
    Postorder Traversal: left -> right -> root
    """
    root = TreeNode(1,
            TreeNode(2, TreeNode(4), TreeNode(5)),
            TreeNode(3)
        )

    result = []

    def postorder(node):
        if not node:
            return
        postorder(node.left)
        postorder(node.right)
        result.append(node.val)

    postorder(root)
    return result

print("Output Example 2:", example_two())
