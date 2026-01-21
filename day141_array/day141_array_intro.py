"""Day 141: Array"""


# Example 1: Minimum moves to equal array elements
def example_one():
    """
    Key idea:
    Incrementing n-1 elements by 1 == decrementing 1 element by 1.
    Answer = sum(nums) - min(nums) * len(nums)
    """
    nums = [1, 2, 3]
    return sum(nums) - min(nums) * len(nums)


print("Output Example 1:", example_one())


# Example 2: Detect 132 pattern using stack
def example_two():
    """
    Traverse from right:
    Maintain decreasing stack and a 'middle' value.
    """
    nums = [3, 1, 4, 2]
    stack = []
    third = float("-inf")

    for n in reversed(nums):
        if n < third:
            return True
        while stack and stack[-1] < n:
            third = stack.pop()
        stack.append(n)

    return False


print("Output Example 2:", example_two())
