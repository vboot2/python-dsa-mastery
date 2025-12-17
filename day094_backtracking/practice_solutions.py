"""
Day 94: Backtracking - LeetCode Problem Solutions
"""

from typing import List

# ---------------------------------------------------------
# Problem 1: 4Sum (LeetCode 18, Medium)
# Link: https://leetcode.com/problems/4sum/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]

                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1

                        # Skip duplicates
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1

                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return res


# ---------------------------------------------------------
# Problem 2: Word Break II (LeetCode 140, Hard)
# Link: https://leetcode.com/problems/word-break-ii/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return [""]

            if i in memo:
                return memo[i]

            res = []

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in word_set:
                    following = dfs(j)
                    for tail in following:
                        if tail == "":
                            res.append(word)
                        else:
                            res.append(word + " " + tail)

            memo[i] = res
            return res

        return dfs(0)


# ---------------------------------------------------------
# Problem 3: Expression Add Operators (LeetCode 282, Hard)
# Link: https://leetcode.com/problems/expression-add-operators/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, num: str, target: int) -> List[str]:
        res = []

        def backtrack(i, path, value, last):
            # i = current index in num
            # path = current expression as string
            # value = current evaluated expression
            # last = last added/subtracted component (for handling multiplication)

            if i == len(num):
                if value == target:
                    res.append(path)
                return

            for j in range(i, len(num)):
                # Avoid numbers like "05"
                if j > i and num[i] == "0":
                    break

                curr_str = num[i:j + 1]
                curr = int(curr_str)

                if i == 0:
                    # First number: Can't add operators before it
                    backtrack(j + 1, curr_str, curr, curr)
                else:
                    # Add +
                    backtrack(j + 1, path + "+" + curr_str, value + curr, curr)

                    # Add -
                    backtrack(j + 1, path + "-" + curr_str, value - curr, -curr)

                    # Add *
                    backtrack(
                        j + 1,
                        path + "*" + curr_str,
                        value - last + last * curr,
                        last * curr
                    )

        backtrack(0, "", 0, 0)
        return res


# =========================================================
# Example usage
# =========================================================
if __name__ == "__main__":
    print("Problem One Example:", SolutionProblemOne().solve([1, 0, -1, 0, -2, 2], 0))
    print("Problem Two Example:", SolutionProblemTwo().solve("catsanddog", ["cat","cats","and","sand","dog"]))
    print("Problem Three Example:", SolutionProblemThree().solve("123", 6))
