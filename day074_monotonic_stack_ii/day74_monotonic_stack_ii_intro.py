"""
Day 74: Monotonic Stack II
"""

# -----------------------------------------------
# Example 1: Largest Rectangle in Histogram
# -----------------------------------------------


def example_one(heights):
    """
    Compute the largest rectangle in a histogram using a monotonic increasing stack.
    Time: O(n)
    """
    stack = []
    max_area = 0
    heights.append(0)  # sentinel to flush remaining bars

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    heights.pop()
    return max_area


print("Output Example 1:", example_one([2, 1, 5, 6, 2, 3]))  # Expected: 10


# -----------------------------------------------
# Example 2: Remove K Digits (Greedy Stack)
# -----------------------------------------------


def example_two(num: str, k: int) -> str:
    """
    Remove k digits from the number to form the smallest possible number.
    Uses a monotonically increasing stack to keep digits minimal.
    """
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # Remove any remaining digits
    final_stack = stack[:-k] if k else stack
    # Strip leading zeros
    result = "".join(final_stack).lstrip("0") or "0"
    return result


print("Output Example 2:", example_two("1432219", 3))  # Expected: "1219"
