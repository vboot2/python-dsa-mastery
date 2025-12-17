""" Day 93: Backtracking  
Backtracking explores all possible choices by building partial solutions and undoing steps (backtrack) when needed.
"""

# Example 1: Generate all subsets of a list
def example_one():
    """
    Classic backtracking pattern:
    - Choose
    - Explore (recurse)
    - Unchoose (backtrack)
    """
    nums = [1, 2, 3]
    result = []
    subset = []

    def backtrack(i):
        if i == len(nums):
            result.append(subset.copy())
            return

        # Choice 1: include nums[i]
        subset.append(nums[i])
        backtrack(i + 1)

        # Undo choice
        subset.pop()

        # Choice 2: skip nums[i]
        backtrack(i + 1)

    backtrack(0)
    return result

print("Output Example 1:", example_one())


# Example 2: Generate all valid parentheses for n=2
def example_two():
    """
    Backtracking with constraints:
    - You can add '(' if left < n
    - You can add ')' if right < left
    """
    n = 2
    result = []

    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return

        if left < n:
            backtrack(s + "(", left + 1, right)
        if right < left:
            backtrack(s + ")", left, right + 1)

    backtrack("", 0, 0)
    return result

print("Output Example 2:", example_two())
