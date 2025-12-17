"""
Day 94: Backtracking
Backtracking is a DFS-based problem-solving technique where we build partial solutions
and undo choices when they lead to invalid outcomes.
"""

# Example 1: Basic Backtracking – Generate all subsets
def example_one():
    # Explore all include / exclude choices
    nums = [1, 2, 3]
    result = []

    def backtrack(i, path):
        if i == len(nums):
            result.append(path[:])
            return

        # Option 1: skip element
        backtrack(i + 1, path)

        # Option 2: include element
        path.append(nums[i])
        backtrack(i + 1, path)

        # Undo choice
        path.pop()

    backtrack(0, [])
    return result

print("Output Example 1:", example_one())


# Example 2: Backtracking with pruning – Combination Sum
def example_two():
    candidates = [2, 3, 6, 7]
    target = 7
    result = []

    def dfs(i, total, path):
        # Prune invalid paths
        if total > target:
            return
        if total == target:
            result.append(path[:])
            return

        for j in range(i, len(candidates)):
            path.append(candidates[j])
            dfs(j, total + candidates[j], path)
            path.pop()

    dfs(0, 0, [])
    return result

print("Output Example 2:", example_two())
