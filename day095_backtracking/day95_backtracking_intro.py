""" 
Day 95: Backtracking  
Backtracking explores decision trees by building partial solutions and undoing choices to explore alternatives.
"""

# Example 1: Generate all combinations that sum to a target
def example_one():
    """
    Classic combination-sum pattern:
    - Choose a number
    - Recurse with reduced target
    - Backtrack
    """
    nums = [2, 3, 6, 7]
    target = 7
    result = []
    path = []

    def backtrack(i, remaining):
        if remaining == 0:
            result.append(path.copy())
            return
        if remaining < 0 or i == len(nums):
            return

        # Choice 1: include nums[i]
        path.append(nums[i])
        backtrack(i, remaining - nums[i])
        path.pop()

        # Choice 2: skip nums[i]
        backtrack(i + 1, remaining)

    backtrack(0, target)
    return result

print("Output Example 1:", example_one())


# Example 2: Letter Case Permutation
def example_two():
    """
    Backtracking where each character can branch into:
    - lowercase (if alpha)
    - uppercase (if alpha)
    - digit (no branch)
    """
    s = "a1b2"
    result = []
    path = []

    def backtrack(i):
        if i == len(s):
            result.append("".join(path))
            return

        c = s[i]
        if c.isalpha():
            # lower
            path.append(c.lower())
            backtrack(i + 1)
            path.pop()

            # upper
            path.append(c.upper())
            backtrack(i + 1)
            path.pop()
        else:
            path.append(c)
            backtrack(i + 1)
            path.pop()

    backtrack(0)
    return result

print("Output Example 2:", example_two())
