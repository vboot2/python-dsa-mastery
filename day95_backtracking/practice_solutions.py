""" Day 95: Backtracking - LeetCode Problem Solutions """

from typing import List


# ---------------------------------------------------------
# Problem: Permutations II (LeetCode 47, Medium)
# Link: https://leetcode.com/problems/permutations-ii/
# ---------------------------------------------------------

class SolutionProblemOne:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking with duplicate control:
        - Sort to group duplicates
        - Skip using "used[i] == used[i-1]" rule
        """
        nums.sort()
        result = []
        used = [False] * len(nums)
        path = []

        def backtrack():
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                # skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    backtrack()

                    path.pop()
                    used[i] = False

        backtrack()
        return result


# ---------------------------------------------------------
# Problem: Beautiful Arrangement (LeetCode 526, Medium)
# Link: https://leetcode.com/problems/beautiful-arrangement/
# ---------------------------------------------------------

class SolutionProblemTwo:
    def countArrangement(self, n: int) -> int:
        """
        Backtracking:
        - For each position i, try all unused numbers j
        - Condition: j % i == 0 OR i % j == 0
        - Use used[] to mark chosen numbers
        """
        used = [False] * (n + 1)
        count = 0

        def backtrack(i):
            nonlocal count
            if i > n:
                count += 1
                return

            for num in range(1, n + 1):
                if not used[num] and (num % i == 0 or i % num == 0):
                    used[num] = True
                    backtrack(i + 1)
                    used[num] = False

        backtrack(1)
        return count


# ---------------------------------------------------------
# Problem: Find All Possible Recipes from Given Supplies (LeetCode 2115, Medium)
# Link: https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
# ---------------------------------------------------------

class SolutionProblemThree:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        """
        Backtracking + dependency resolution:
        - Treat recipes as nodes, ingredients as dependencies.
        - Use DFS to check if recipe can be formed.
        - Use memo to avoid repeated work.
        - Detect cycles to prevent infinite recursion.
        """
        recipe_map = {recipe: ing for recipe, ing in zip(recipes, ingredients)}
        supply_set = set(supplies)
        memo = {}
        visiting = set()

        def can_make(item):
            if item in supply_set:
                return True
            if item not in recipe_map:
                return False
            if item in memo:
                return memo[item]
            if item in visiting:  # cycle detected
                return False

            visiting.add(item)

            for ing in recipe_map[item]:
                if not can_make(ing):
                    memo[item] = False
                    visiting.remove(item)
                    return False

            visiting.remove(item)
            memo[item] = True
            return True

        result = []
        for r in recipes:
            if can_make(r):
                result.append(r)
        return result


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().permuteUnique([1, 1, 2]))
    print("Problem Two Example:", SolutionProblemTwo().countArrangement(3))
    print("Problem Three Example:", SolutionProblemThree().findAllRecipes(
        ["bread"], [["yeast", "flour"]], ["yeast", "flour"]
    ))
