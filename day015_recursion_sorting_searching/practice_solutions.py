"""
Day 15: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Permutations (LeetCode 46, Medium)
# Link: https://leetcode.com/problems/permutations/
# ---------------------------------------------------------
class SolutionPermutations:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
                    used[i] = False

        backtrack([])
        return res


# ---------------------------------------------------------
# Problem 2: Combinations (LeetCode 77, Medium)
# Link: https://leetcode.com/problems/combinations/
# ---------------------------------------------------------
class SolutionCombinations:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return res


# ---------------------------------------------------------
# Problem 3: Subsets (LeetCode 78, Medium)
# Link: https://leetcode.com/problems/subsets/
# ---------------------------------------------------------
class SolutionSubsets:
    def subsets(self, nums: list[int]) -> list[list[int]]:
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
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Permutations of [1,2,3]:", SolutionPermutations().permute([1,2,3]))
    print("Combinations of 4 choose 2:", SolutionCombinations().combine(4,2))
    print("Subsets of [1,2,3]:", SolutionSubsets().subsets([1,2,3]))
