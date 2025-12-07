""" 
Day 98: Matrix / Tree - LeetCode Problem Solutions 
"""
from typing import List, Optional

# ---------------------------------------------------------
# Problem: Spiral Matrix (LeetCode 54, Medium)
# Link: https://leetcode.com/problems/spiral-matrix/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # traverse top row
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1

            # traverse right col
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                # traverse bottom row
                for c in range(right, left - 1, -1):
                    res.append(matrix[bottom][c])
                bottom -= 1

            if left <= right:
                # traverse left col
                for r in range(bottom, top - 1, -1):
                    res.append(matrix[r][left])
                left += 1

        return res


# ---------------------------------------------------------
# Problem: First Missing Positive (LeetCode 41, Hard)
# Link: https://leetcode.com/problems/first-missing-positive/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, nums: List[int]) -> int:
        """
        Index-as-hash approach. Place each number at index value-1.
        """
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # swap nums[i] with nums[val-1]
                correct_pos = nums[i] - 1
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1


# ---------------------------------------------------------
# Problem: House Robber III (LeetCode 337, Medium)
# Link: https://leetcode.com/problems/house-robber-iii/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionProblemThree:
    def solve(self, root: Optional[TreeNode]) -> int:
        """
        Return max rob value using DFS:
        Each node returns (rob_this, skip_this).
        """

        def dfs(node):
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            skip = max(left) + max(right)
            return (rob, skip)

        return max(dfs(root))


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().solve([[1,2,3],[4,5,6],[7,8,9]]))
    print("Problem Two Example:", SolutionProblemTwo().solve([3,4,-1,1]))

    # Tree for Problem 3:     3
    #                        / \
    #                       2   3
    root = TreeNode(3, TreeNode(2), TreeNode(3))
    print("Problem Three Example:", SolutionProblemThree().solve(root))
