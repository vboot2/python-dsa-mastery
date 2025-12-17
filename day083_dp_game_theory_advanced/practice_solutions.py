"""
Day 83: DP Game Theory / Advanced – LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Predict the Winner (LeetCode 486, Medium)
# Link: https://leetcode.com/problems/predict-the-winner/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, nums):
        from functools import lru_cache

        @lru_cache(None)
        def dp(l, r):
            if l == r:
                return nums[l]

            # Score difference current player can achieve
            left = nums[l] - dp(l+1, r)
            right = nums[r] - dp(l, r-1)
            return max(left, right)

        return dp(0, len(nums)-1) >= 0


# ---------------------------------------------------------
# Problem: Longest String Chain (LeetCode 1048, Medium)
# Link: https://leetcode.com/problems/longest-string-chain/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, words):
        words.sort(key=len)
        dp = {}
        longest = 1

        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                pred = w[:i] + w[i+1:]
                if pred in dp:
                    dp[w] = max(dp[w], dp[pred] + 1)
            longest = max(longest, dp[w])

        return longest


# ---------------------------------------------------------
# Problem: Odd Even Jump (LeetCode 975, Hard)
# Link: https://leetcode.com/problems/odd-even-jump/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, arr):
        n = len(arr)
        import bisect

        # Next greater (odd jumps)
        # Next smaller (even jumps)
        sorted_idx = sorted(range(n), key=lambda i: (arr[i], i))
        next_greater = [None]*n
        stack = []
        for i in sorted_idx:
            while stack and i > stack[-1]:
                next_greater[stack.pop()] = i
            stack.append(i)

        sorted_idx = sorted(range(n), key=lambda i: (-arr[i], i))
        next_smaller = [None]*n
        stack = []
        for i in sorted_idx:
            while stack and i > stack[-1]:
                next_smaller[stack.pop()] = i
            stack.append(i)

        # DP
        odd = [False]*n
        even = [False]*n
        odd[-1] = even[-1] = True

        for i in range(n-2, -1, -1):
            if next_greater[i] is not None:
                odd[i] = even[next_greater[i]]
            if next_smaller[i] is not None:
                even[i] = odd[next_smaller[i]]

        return sum(odd)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().solve([1, 5, 2]))

    print("Problem Two Example:",
          SolutionProblemTwo().solve(["a","ba","bca","bda","bdca"]))

    print("Problem Three Example:",
          SolutionProblemThree().solve([10,13,12,14,15]))
