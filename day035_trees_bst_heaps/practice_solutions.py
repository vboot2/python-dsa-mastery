"""
Day 35: Trees, BST, Heaps - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Sum Root to Leaf Numbers (LeetCode 129, Medium)
# Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionSumNumbers:
    def sumNumbers(self, root):
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                return curr_sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        return dfs(root, 0)


# ---------------------------------------------------------
# Problem 2: Path Sum III (LeetCode 437, Medium)
# Link: https://leetcode.com/problems/path-sum-iii/
# ---------------------------------------------------------
class SolutionPathSumIII:
    def pathSum(self, root, targetSum: int) -> int:
        prefix_sums = {0: 1}

        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum += node.val
            count = prefix_sums.get(curr_sum - targetSum, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            prefix_sums[curr_sum] -= 1
            return count

        return dfs(root, 0)


# ---------------------------------------------------------
# Problem 3: Count Good Nodes in Binary Tree (LeetCode 1448, Medium)
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# ---------------------------------------------------------
class SolutionGoodNodes:
    def goodNodes(self, root) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            count = 1 if node.val >= max_val else 0
            max_val = max(max_val, node.val)
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            return count
        return dfs(root, float('-inf'))


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    print("Sum Root to Leaf Numbers:", SolutionSumNumbers().sumNumbers(root1))

    root2 = TreeNode(10, 
        TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
        TreeNode(-3, None, TreeNode(11))
    )
    print("Path Sum III:", SolutionPathSumIII().pathSum(root2, 8))

    root3 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print("Good Nodes Count:", SolutionGoodNodes().goodNodes(root3))
