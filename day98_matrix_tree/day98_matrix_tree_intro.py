"""
Day 98: Matrix / Tree
Understanding matrix traversal (spiral order), index/value mapping tricks,
and dynamic programming over trees (House Robber III).
"""

# ---------------------------------------------------------
# Example 1: Spiral traversal of a matrix
# ---------------------------------------------------------
def example_one():
    """
    Demonstrates spiral order traversal using boundaries.
    """
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            res.append(matrix[top][c])
        top += 1

        for r in range(top, bottom + 1):
            res.append(matrix[r][right])
        right -= 1

        if top <= bottom:
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1

        if left <= right:
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1

    return res

print("Output Example 1:", example_one())


# ---------------------------------------------------------
# Example 2: Tree DP – Return (rob, not_rob) for each node
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_two():
    """
    Demonstrates the idea behind House Robber III DP.
    For each node: return tuple (rob_this, skip_this).
    """
    # Tree:
    #     3
    #    / \
    #   2   3
    root = TreeNode(3, TreeNode(2), TreeNode(3))

    def dfs(node):
        if not node:
            return (0, 0)

        left = dfs(node.left)
        right = dfs(node.right)

        rob = node.val + left[1] + right[1]
        skip = max(left) + max(right)
        return (rob, skip)

    return max(dfs(root))

print("Output Example 2:", example_two())
