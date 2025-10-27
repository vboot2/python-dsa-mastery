"""
Day 57: Backtracking (Advanced)
"""

# ---------------------------------------------------------
# Example 1: Generate all subsets
# ---------------------------------------------------------


def example_one(nums):
    """
    Generate all possible subsets using backtracking.
    """
    res = []

    def backtrack(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res


# ---------------------------------------------------------
# Example 2: String permutations
# ---------------------------------------------------------


def example_two(s):
    """
    Generate all permutations of a string using backtracking.
    """
    res = []
    chars = list(s)
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            res.append("".join(path))
            return
        for i in range(len(chars)):
            if not used[i]:
                used[i] = True
                path.append(chars[i])
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return res


# Example runs
print("Example 1 (Subsets):", example_one([1, 2, 3]))
print("Example 2 (Permutations):", example_two("ABC"))
