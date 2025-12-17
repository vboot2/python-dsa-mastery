"""
Day 64: Bit Manipulation - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Number of 1 Bits (LeetCode 191, Easy)
# Link: https://leetcode.com/problems/number-of-1-bits/
# ---------------------------------------------------------


class SolutionNumberOf1Bits:
    def hammingWeight(self, n: int) -> int:
        # Brian Kernighan's Algorithm - repeatedly clear lowest set bit
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


# ---------------------------------------------------------
# Problem 2: Missing Number (LeetCode 268, Easy)
# Link: https://leetcode.com/problems/missing-number/
# ---------------------------------------------------------


class SolutionMissingNumber:
    def missingNumber(self, nums: list[int]) -> int:
        # XOR all indices and numbers — pairs cancel, leaving the missing number
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


# ---------------------------------------------------------
# Problem 3: Counting Bits (LeetCode 338, Easy)
# Link: https://leetcode.com/problems/counting-bits/
# ---------------------------------------------------------


class SolutionCountingBits:
    def countBits(self, n: int) -> list[int]:
        # DP approach: bits[i] = bits[i >> 1] + (i & 1)
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i >> 1] + (i & 1)
        return bits


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Number of 1 bits in 11:", SolutionNumberOf1Bits().hammingWeight(11))
    print(
        "Missing number from [3,0,1]:", SolutionMissingNumber().missingNumber([3, 0, 1])
    )
    print("Counting bits up to 5:", SolutionCountingBits().countBits(5))
