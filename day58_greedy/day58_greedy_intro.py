"""
Day 58: Greedy Algorithms
"""


# Example 1: Activity Selection (Maximize non-overlapping intervals)
def example_one():
    # Each activity is represented as (start, end)
    activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
    # Sort by end time
    activities.sort(key=lambda x: x[1])
    selected = []
    last_end = 0

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end
    return selected


print("Output Example 1:", example_one())


# Example 2: Minimum Number of Coins (Classic Greedy Problem)
def example_two():
    coins = [1, 2, 5, 10, 20, 50, 100]
    amount = 93
    result = []
    for coin in reversed(coins):
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result


print("Output Example 2:", example_two())
