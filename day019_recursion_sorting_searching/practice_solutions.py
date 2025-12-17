"""
Day 19: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Decode Ways (LeetCode 91, Medium)
# Link: https://leetcode.com/problems/decode-ways/
# ---------------------------------------------------------
class SolutionDecodeWays:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            res = dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i+2)

            memo[i] = res
            return res

        return dfs(0)


# ---------------------------------------------------------
# Problem 2: Unique Binary Search Trees II (LeetCode 95, Medium)
# Link: https://leetcode.com/problems/unique-binary-search-trees-ii/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionUniqueBST:
    def generateTrees(self, n: int):
        if n == 0:
            return []

        def build(start, end):
            if start > end:
                return [None]

            all_trees = []
            for root_val in range(start, end + 1):
                left_trees = build(start, root_val - 1)
                right_trees = build(root_val + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(root_val)
                        root.left = l
                        root.right = r
                        all_trees.append(root)

            return all_trees

        return build(1, n)


# ---------------------------------------------------------
# Problem 3: Different Ways to Add Parentheses (LeetCode 241, Medium)
# Link: https://leetcode.com/problems/different-ways-to-add-parentheses/
# ---------------------------------------------------------
class SolutionDifferentWays:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, ch in enumerate(expression):
            if ch in "+-*":
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if ch == "+":
                            res.append(l+r)
                        elif ch == "-":
                            res.append(l-r)
                        else:
                            res.append(l*r)
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Decode Ways:", SolutionDecodeWays().numDecodings("226"))
    print("Unique BSTs (n=3):", len(SolutionUniqueBST().generateTrees(3)))
    print("Different Ways to Compute:", SolutionDifferentWays().diffWaysToCompute("2*3-4*5"))
