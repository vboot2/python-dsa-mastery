"""Day 144: DFS
Depth-First Search explores a path fully before backtracking.
DFS is commonly used in trees, graphs, recursion problems,
and structure reconstruction.
"""


# Example 1: DFS on binary tree (preorder)
def example_one():
    """
    Preorder DFS:
    Root -> Left -> Right
    """

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = TreeNode(1, TreeNode(2), TreeNode(3))
    result = []

    def dfs(node):
        if not node:
            return
        result.append(node.val)
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return result


print("Output Example 1:", example_one())


# Example 2: DFS on nested structure
def example_two():
    """
    Recursively parse nested lists.
    """
    data = [1, [2, [3, 4]], 5]
    res = []

    def dfs(item):
        if isinstance(item, int):
            res.append(item)
        else:
            for x in item:
                dfs(x)

    dfs(data)
    return res


print("Output Example 2:", example_two())
