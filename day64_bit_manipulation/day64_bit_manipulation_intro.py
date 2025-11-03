"""
Day 64: Bit Manipulation
"""


# -------------------------------
# Example 1: Counting set bits in an integer (Brian Kernighan’s Algorithm)
# -------------------------------
def example_one(n: int) -> int:
    # Count number of 1s in binary representation
    count = 0
    while n:
        n &= n - 1  # drops the lowest set bit
        count += 1
    return count


print("Output Example 1 (set bits in 29):", example_one(29))  # 29 = 11101 → 4 set bits


# -------------------------------
# Example 2: Checking if a number is power of two
# -------------------------------
def example_two(n: int) -> bool:
    # A number is power of two if only one bit is set in its binary form
    return n > 0 and (n & (n - 1)) == 0


print("Output Example 2 (is 16 power of two?):", example_two(16))
print("Output Example 2 (is 18 power of two?):", example_two(18))


# -------------------------------
# Example 3: Swapping two numbers without using a temp variable
# -------------------------------
def example_three(a: int, b: int) -> tuple[int, int]:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


print("Output Example 3 (swap 5 and 9):", example_three(5, 9))
