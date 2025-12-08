""" 
Day 99: Tree / DP - LeetCode Problem Solutions 
"""
from typing import List, Optional
from collections import defaultdict


# ---------------------------------------------------------
# Problem: Find Mode in Binary Search Tree (LeetCode 501, Easy)
# Link: https://leetcode.com/problems/find-mode-in-binary-search-tree/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionProblemOne:
    def solve(self, root: Optional[TreeNode]) -> List[int]:
        """
        Inorder traversal produces sorted order; count frequencies.
        """
        self.prev = None
        self.count = 0
        self.max_count = 0
        modes = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            # If same value, increment count
            if node.val == self.prev:
                self.count += 1
            else:
                self.prev = node.val
                self.count = 1

            # Track max freq
            if self.count > self.max_count:
                self.max_count = self.count
                modes.clear()
                modes.append(node.val)
            elif self.count == self.max_count:
                modes.append(node.val)

            inorder(node.right)

        inorder(root)
        return modes


# ---------------------------------------------------------
# Problem: Number of Good Leaf Pairs (LeetCode 1530, Medium)
# Link: https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, root: Optional[TreeNode], distance: int) -> int:
        """
        DFS returns list of leaf distances.
        Count valid pairs (d1 + d2 <= distance).
        """
        self.count = 0

        def dfs(node):
            if not node:
                return []

            if not node.left and not node.right:
                return [1]

            left_dist = dfs(node.left)
            right_dist = dfs(node.right)

            # Count valid pairs
            for ld in left_dist:
                for rd in right_dist:
                    if ld + rd <= distance:
                        self.count += 1

            # Return incremented distances upward
            new_dist = []
            for d in left_dist + right_dist:
                if d + 1 <= distance:
                    new_dist.append(d + 1)

            return new_dist

        dfs(root)
        return self.count


# ---------------------------------------------------------
# Problem: Best Time to Buy and Sell Stock with Cooldown (LeetCode 309, Medium)
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, prices: List[int]) -> int:
        """
        Classic DP:
        dp[i][0] = holding
        dp[i][1] = not holding (no cooldown)
        dp[i][2] = just sold (cooldown)
        """
        if not prices:
            return 0

        n = len(prices)

        hold = -prices[0]
        no_hold = 0
        cooldown = 0

        for p in prices[1:]:
            new_hold = max(hold, no_hold - p)
            new_no_hold = max(no_hold, cooldown)
            new_cooldown = hold + p

            hold, no_hold, cooldown = new_hold, new_no_hold, new_cooldown

        return max(no_hold, cooldown)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    # Problem 1
    root = TreeNode(1, None, TreeNode(2, TreeNode(2)))
    print("Problem One Example:", SolutionProblemOne().solve(root))

    # Problem 2
    print("Problem Two Example:", SolutionProblemTwo().solve(root, 3))

    # Problem 3
    print("Problem Three Example:", SolutionProblemThree().solve([1,2,3,0,2]))
