"""
Day 65: Bit Manipulation II - LeetCode Problem Solutions
"""


# ---------------------------------------------------------
# Problem 1: Single Number II (LeetCode 137, Medium)
# Link: https://leetcode.com/problems/single-number-ii/
# ---------------------------------------------------------
class SolutionSingleNumberII:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in range(32):
            bit_sum = sum((num >> i) & 1 for num in nums)
            if bit_sum % 3:
                result |= 1 << i
        if result >= 2**31:
            result -= 2**32
        return result


# ---------------------------------------------------------
# Problem 2: Single Number III (LeetCode 260, Medium)
# Link: https://leetcode.com/problems/single-number-iii/
# ---------------------------------------------------------
class SolutionSingleNumberIII:
    def singleNumber(self, nums: list[int]) -> list[int]:
        xor_all = 0
        for n in nums:
            xor_all ^= n

        diff_bit = xor_all & -xor_all

        a = b = 0
        for n in nums:
            if n & diff_bit:
                a ^= n
            else:
                b ^= n

        return [a, b]


# ---------------------------------------------------------
# Problem 3: Sum of Two Integers (LeetCode 371, Medium)
# Link: https://leetcode.com/problems/sum-of-two-integers/
# ---------------------------------------------------------
class SolutionSumTwoIntegers:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK
        return a if a <= MAX_INT else ~(a ^ MASK)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "Single Number II [2,2,3,2]:",
        SolutionSingleNumberII().singleNumber([2, 2, 3, 2]),
    )
    print(
        "Single Number III [1,2,1,3,2,5]:",
        SolutionSingleNumberIII().singleNumber([1, 2, 1, 3, 2, 5]),
    )
    print("Sum of Two Integers (5, -3):", SolutionSumTwoIntegers().getSum(5, -3))
