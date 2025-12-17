"""
Day 54: Trees + DFS
Exploring Depth-First Search (DFS) on binary trees to find root-to-leaf paths and path sums.
"""


# Example 1: Basic DFS traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs_inorder(root):
    if not root:
        return []
    return dfs_inorder(root.left) + [root.val] + dfs_inorder(root.right)


# Example 2: Path Sum Check
def has_path_sum(root, target_sum):
    if not root:
        return False
    if not root.left and not root.right and root.val == target_sum:
        return True
    return has_path_sum(root.left, target_sum - root.val) or has_path_sum(
        root.right, target_sum - root.val
    )


# Building a small example tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)

print("Inorder Traversal:", dfs_inorder(root))
print("Has Path Sum (22):", has_path_sum(root, 22))
