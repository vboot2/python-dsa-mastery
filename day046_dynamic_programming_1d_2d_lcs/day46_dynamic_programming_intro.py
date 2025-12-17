"""
Day 46: Dynamic Programming (1D, 2D, LCS)
"""

# ----------------------------------------
# Example 1: Word Break
# ----------------------------------------
def example_one():
    s = "leetcode"
    wordDict = {"leet", "code"}
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for w in wordDict:
            if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                dp[i] = True
    return dp[-1]

print("Output Example 1 (Word Break):", example_one())


# ----------------------------------------
# Example 2: Target Sum
# ----------------------------------------
def example_two():
    nums = [1, 1, 1, 1, 1]
    target = 3
    total = sum(nums)
    if (target + total) % 2 != 0 or target > total:
        return 0
    subset_sum = (target + total) // 2
    dp = [0] * (subset_sum + 1)
    dp[0] = 1

    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]
    return dp[-1]

print("Output Example 2 (Target Sum):", example_two())


# ----------------------------------------
# Example 3: Coin Change II
# ----------------------------------------
def example_three():
    coins = [1, 2, 5]
    amount = 5
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]

print("Output Example 3 (Coin Change II):", example_three())
