""" Day 120: String
String problems here focus on directional movement, palindrome validation,
counting grouped characters, and simple character transformations.
"""

# Example 1: Check if robot returns to origin
def example_one():
    """
    Track movement using coordinate changes.
    U/D affect y-axis, L/R affect x-axis.
    """
    moves = "UDLR"
    x = y = 0

    for m in moves:
        if m == 'U':
            y += 1
        elif m == 'D':
            y -= 1
        elif m == 'L':
            x -= 1
        elif m == 'R':
            x += 1

    return x == 0 and y == 0

print("Output Example 1:", example_one())


# Example 2: Check if string is almost a palindrome
def example_two():
    """
    Two-pointer technique:
    - Allow at most one character removal
    """
    s = "abca"

    def is_pal(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_pal(left + 1, right) or is_pal(left, right - 1)
        left += 1
        right -= 1

    return True

print("Output Example 2:", example_two())
