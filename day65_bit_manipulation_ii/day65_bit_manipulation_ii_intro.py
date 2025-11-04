"""
Day 65: Bit Manipulation II
"""


# -------------------------------
# Example 1: Single Number II (every element appears thrice except one)
# -------------------------------
def example_one(nums: list[int]) -> int:
    # Count bits at each position; take mod 3 to isolate unique element
    result = 0
    for i in range(32):
        bit_sum = sum((num >> i) & 1 for num in nums)
        if bit_sum % 3:
            result |= 1 << i
    # Handle negative numbers (32-bit adjustment)
    if result >= 2**31:
        result -= 2**32
    return result


print("Output Example 1 ([2,2,3,2]):", example_one([2, 2, 3, 2]))


# -------------------------------
# Example 2: Two Single Numbers (every element appears twice except two)
# -------------------------------
def example_two(nums: list[int]) -> tuple[int, int]:
    xor_all = 0
    for n in nums:
        xor_all ^= n
    # Get rightmost set bit (distinguishing factor between two unique numbers)
    diff_bit = xor_all & -xor_all
    a = b = 0
    for n in nums:
        if n & diff_bit:
            a ^= n
        else:
            b ^= n
    return a, b


print("Output Example 2 ([1,2,1,3,2,5]):", example_two([1, 2, 1, 3, 2, 5]))


# -------------------------------
# Example 3: Sum of Two Integers without '+' or '-'
# -------------------------------
def example_three(a: int, b: int) -> int:
    # Use bitwise operations for addition
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF
    while b != 0:
        carry = (a & b) & MASK
        a = (a ^ b) & MASK
        b = (carry << 1) & MASK
    # Convert from unsigned to signed
    return a if a <= MAX_INT else ~(a ^ MASK)


print("Output Example 3 (Sum of 5 and -3):", example_three(5, -3))
