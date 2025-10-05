"""
Day 35: Trees, BST, Heaps

Recursive tree traversal problems focusing on path sums and node comparisons.
- Sum Root to Leaf Numbers - DFS with path accumulation
- Path Sum III - DFS + prefix sum
- Count Good Nodes in Binary Tree - DFS with tracking of max value on path
"""

# -------------------------------
# Example 1: Sum Root to Leaf Numbers
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root: TreeNode) -> int:
    def dfs(node, current_sum):
        if not node:
            return 0
        current_sum = current_sum * 10 + node.val
        if not node.left and not node.right:
            return current_sum
        return dfs(node.left, current_sum) + dfs(node.right, current_sum)
    return dfs(root, 0)

# Example tree: [1, 2, 3] → 12 + 13 = 25
root = TreeNode(1, TreeNode(2), TreeNode(3))
print("Sum Root to Leaf Numbers:", sum_numbers(root))


# -------------------------------
# Example 2: Path Sum III
# -------------------------------
def path_sum(root: TreeNode, target_sum: int) -> int:
    prefix_sums = {0: 1}
    
    def dfs(node, curr_sum):
        if not node:
            return 0
        curr_sum += node.val
        count = prefix_sums.get(curr_sum - target_sum, 0)
        prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
        count += dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        prefix_sums[curr_sum] -= 1
        return count
    
    return dfs(root, 0)

# Example tree: [10,5,-3,3,2,None,11,3,-2,None,1], target = 8 → Output: 3
root = TreeNode(10, 
    TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
    TreeNode(-3, None, TreeNode(11))
)
print("Path Sum III:", path_sum(root, 8))


# -------------------------------
# Example 3: Count Good Nodes in Binary Tree
# -------------------------------
def good_nodes(root: TreeNode) -> int:
    def dfs(node, max_val):
        if not node:
            return 0
        count = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)
        return count
    return dfs(root, float('-inf'))

# Example tree: [3,1,4,3,None,1,5] → Output: 4
root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
print("Count Good Nodes:", good_nodes(root))
