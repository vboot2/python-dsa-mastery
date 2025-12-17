"""
Day 99: Tree / DP
Covers tree traversal with frequency tracking (BST mode),
counting good leaf pairs using DFS aggregation, and dynamic programming
with state transitions (Stock DP – cooldown).
"""

# ---------------------------------------------------------
# Example 1: Simple BST inorder traversal with value frequency map
# ---------------------------------------------------------
def example_one():
    """
    Demonstrates BST inorder + frequency counting.
    """
    from collections import defaultdict

    # Example tree (not using TreeNode class for simplicity)
    vals = [1, 2, 2, 3, 3, 3]
    freq = defaultdict(int)

    for v in vals:
        freq[v] += 1

    # Modes are values with highest frequency
    max_freq = max(freq.values())
    modes = [k for k, v in freq.items() if v == max_freq]

    return modes

print("Output Example 1:", example_one())


# ---------------------------------------------------------
# Example 2: Tree DP aggregation example – return list of leaf depths
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_two():
    """
    Demonstrates how DFS returns arrays upward (like LC 1530).
    Each node returns a list of leaf-depth distances.
    """
    root = TreeNode(1,
                    TreeNode(2,
                             TreeNode(4),
                             TreeNode(5)),
                    TreeNode(3))

    def dfs(node):
        if not node:
            return []

        if not node.left and not node.right:
            return [1]  # leaf distance 1

        left_dist = dfs(node.left)
        right_dist = dfs(node.right)

        # increment all distances before returning upward
        left_dist = [d + 1 for d in left_dist]
        right_dist = [d + 1 for d in right_dist]

        return left_dist + right_dist

    return dfs(root)

print("Output Example 2:", example_two())
