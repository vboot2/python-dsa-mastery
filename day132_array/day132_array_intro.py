"""Day 132: Array
Array counting, prefix/suffix logic,
coordinate geometry, and classic matrix transformations.
"""


# Example 1: Replace elements with greatest element on right
def example_one():
    """
    Traverse from right, keep track of max seen so far.
    """
    arr = [17, 18, 5, 4, 6, 1]
    max_right = -1

    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_right
        max_right = max(max_right, temp)

    return arr


print("Output Example 1:", example_one())


# Example 2: Shift grid elements to the right
def example_two():
    """
    Flatten grid -> shift -> rebuild grid.
    """
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 1

    rows, cols = len(grid), len(grid[0])
    flat = [num for row in grid for num in row]

    k %= len(flat)
    flat = flat[-k:] + flat[:-k]

    return [flat[i * cols : (i + 1) * cols] for i in range(rows)]


print("Output Example 2:", example_two())
