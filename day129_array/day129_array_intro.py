"""Day 129: Array
Focus on array manipulation, simulation, geometry basics,
and matrix transformations.
"""


# Example 1: Reverse each row of a matrix
def example_one():
    """
    In-place reversal of rows using two pointers.
    """
    matrix = [[1, 2, 3], [4, 5, 6]]
    for row in matrix:
        left, right = 0, len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
    return matrix


print("Output Example 1:", example_one())


# Example 2: Lemonade change simulation
def example_two():
    """
    Greedy simulation with bill counting.
    """
    bills = [5, 5, 5, 10, 20]
    five = ten = 0

    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            five -= 1
            ten += 1
        else:
            if ten > 0:
                ten -= 1
                five -= 1
            else:
                five -= 3
        if five < 0:
            return False

    return True


print("Output Example 2:", example_two())
