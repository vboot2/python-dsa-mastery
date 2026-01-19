"""Day 139: Array
Array techniques including prefix sums, range queries,
greedy patterns, dynamic programming, and sweep line methods.
"""


# Example 1: 2D Prefix Sum Query
def example_one():
    """
    Build prefix sum matrix to answer sum queries in O(1).
    """
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]
    r1, c1, r2, c2 = 2, 1, 4, 3

    rows, cols = len(matrix), len(matrix[0])
    ps = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(rows):
        for j in range(cols):
            ps[i + 1][j + 1] = matrix[i][j] + ps[i][j + 1] + ps[i + 1][j] - ps[i][j]

    return ps[r2 + 1][c2 + 1] - ps[r1][c2 + 1] - ps[r2 + 1][c1] + ps[r1][c1]


print("Output Example 1:", example_one())


# Example 2: Increasing triplet detection
def example_two():
    """
    Track smallest and second smallest values greedily.
    """
    nums = [2, 1, 5, 0, 4, 6]
    first = second = float("inf")

    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
    return False


print("Output Example 2:", example_two())
