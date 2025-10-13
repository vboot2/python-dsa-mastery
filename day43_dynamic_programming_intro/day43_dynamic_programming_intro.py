"""
Day 43: Dynamic Programming

Dynamic Programming (DP) breaks problems into overlapping subproblems
and stores results to avoid recomputation. Commonly used for optimization
and counting problems.
"""

# -------------------------------
# Example 1: Fibonacci with Memoization
# -------------------------------
def example_one():
    memo = {}
    def fib(n):
        if n <= 1:
            return n
        if n not in memo:
            memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
    return fib(10)  # Fibonacci(10)

print("Output Example 1 (Fibonacci with Memoization):", example_one())


# -------------------------------
# Example 2: Climbing Stairs (Tabulation)
# -------------------------------
def example_two():
    n = 5
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print("Output Example 2 (Climbing Stairs ways):", example_two())
