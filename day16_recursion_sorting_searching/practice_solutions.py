"""
Day 16: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Combination Sum (LeetCode 39, Medium)
# Link: https://leetcode.com/problems/combination-sum/
# ---------------------------------------------------------
class SolutionCombinationSum:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # reuse allowed
                path.pop()

        backtrack(0, [], 0)
        return res


# ---------------------------------------------------------
# Problem 2: Combination Sum II (LeetCode 40, Medium)
# Link: https://leetcode.com/problems/combination-sum-ii/
# ---------------------------------------------------------
class SolutionCombinationSumII:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return
            prev = -1
            for i in range(start, len(candidates)):
                if candidates[i] == prev:
                    continue
                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])  # no reuse
                path.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res


# ---------------------------------------------------------
# Problem 3: Subsets II (LeetCode 90, Medium)
# Link: https://leetcode.com/problems/subsets-ii/
# ---------------------------------------------------------
class SolutionSubsetsII:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Combination Sum:", SolutionCombinationSum().combinationSum([2,3,6,7], 7))
    print("Combination Sum II:", SolutionCombinationSumII().combinationSum2([10,1,2,7,6,1,5], 8))
    print("Subsets II:", SolutionSubsetsII().subsetsWithDup([1,2,2]))
