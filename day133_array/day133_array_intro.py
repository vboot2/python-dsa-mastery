"""Day 133: Array
Counting techniques, sorting with custom rules, matrix scanning,
and classic in-place array/matrix transformations.
"""


# Example 1: Sum of n unique integers equals zero
def example_one():
    """
    Pair positive and negative numbers.
    If n is odd, include zero.
    """
    n = 5
    result = []
    x = 1

    while len(result) < n:
        if len(result) + 2 <= n:
            result.extend([x, -x])
            x += 1
        else:
            result.append(0)

    return result


print("Output Example 1:", example_one())


# Example 2: Count negative numbers in a sorted matrix
def example_two():
    """
    Since rows and columns are sorted,
    scan from top-right corner.
    """
    grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    rows, cols = len(grid), len(grid[0])
    r, c = 0, cols - 1
    count = 0

    while r < rows and c >= 0:
        if grid[r][c] < 0:
            count += rows - r
            c -= 1
        else:
            r += 1

    return count


print("Output Example 2:", example_two())
