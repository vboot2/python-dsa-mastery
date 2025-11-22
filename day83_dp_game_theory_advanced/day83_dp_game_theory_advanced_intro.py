"""
Day 83: DP – Game Theory / Advanced
- Minimax-style DP for two-player games
- DAG longest chain DP
- Alternating parity DP in arrays
"""

# Example 1: Game DP — Predict Winner (simple minimax)
def example_one():
    nums = [1, 5, 2]
    n = len(nums)

    from functools import lru_cache

    @lru_cache(None)
    def dp(l, r):
        if l == r:
            return nums[l]
        # player can take left or right: choose best score difference
        take_left = nums[l] - dp(l+1, r)
        take_right = nums[r] - dp(l, r-1)
        return max(take_left, take_right)

    return dp(0, n-1) >= 0

print("Output Example 1:", example_one())


# Example 2: DAG DP – longest chain in strings by deletion
def example_two():
    words = ["a", "ba", "bca", "bda", "bdca"]
    words.sort(key=len)
    dp = {}
    best = 1

    for w in words:
        dp[w] = 1
        for i in range(len(w)):
            pred = w[:i] + w[i+1:]
            if pred in dp:
                dp[w] = max(dp[w], dp[pred] + 1)
        best = max(best, dp[w])

    return best

print("Output Example 2:", example_two())
