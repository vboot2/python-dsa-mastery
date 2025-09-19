"""
Day 19: Recursion, Sorting, Searching

"""

# -------------------------------
# Example 1: Decode ways (recursive with memoization)
# -------------------------------
def num_decodings(s: str) -> int:
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

print("Decode Ways for '226':", num_decodings("226"))


# -------------------------------
# Example 2: Generate unique BST counts
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def generate_trees(n: int):
    if n == 0:
        return []

    def build(start, end):
        if start > end:
            return [None]
        all_trees = []
        for root_val in range(start, end+1):
            left_trees = build(start, root_val-1)
            right_trees = build(root_val+1, end)
            for l in left_trees:
                for r in right_trees:
                    root = TreeNode(root_val)
                    root.left = l
                    root.right = r
                    all_trees.append(root)
        return all_trees

    return build(1, n)

print("Number of Unique BSTs for n=3:", len(generate_trees(3)))


# -------------------------------
# Example 3: Different ways to add parentheses
# -------------------------------
def diff_ways_to_compute(expression: str) -> list[int]:
    if expression.isdigit():
        return [int(expression)]

    res = []
    for i, ch in enumerate(expression):
        if ch in "+-*":
            left = diff_ways_to_compute(expression[:i])
            right = diff_ways_to_compute(expression[i+1:])
            for l in left:
                for r in right:
                    if ch == "+":
                        res.append(l+r)
                    elif ch == "-":
                        res.append(l-r)
                    else:
                        res.append(l*r)
    return res

print("Different ways to compute '2*3-4*5':", diff_ways_to_compute("2*3-4*5"))
