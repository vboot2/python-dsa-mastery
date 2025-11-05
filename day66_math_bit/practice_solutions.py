"""
Day 66: Math / Bit - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Pow(x, n) (LeetCode 50, Medium)
# Link: https://leetcode.com/problems/powx-n/
# ---------------------------------------------------------


class SolutionPowXN:
    def myPow(self, x: float, n: int) -> float:
        # Fast exponentiation by squaring
        if n < 0:
            x = 1 / x
            n = -n
        result = 1
        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result


# ---------------------------------------------------------
# Problem 2: Add Binary (LeetCode 67, Easy)
# Link: https://leetcode.com/problems/add-binary/
# ---------------------------------------------------------


class SolutionAddBinary:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a) - 1, len(b) - 1, 0
        res = []
        while i >= 0 or j >= 0 or carry:
            bit_sum = carry
            if i >= 0:
                bit_sum += int(a[i])
                i -= 1
            if j >= 0:
                bit_sum += int(b[j])
                j -= 1
            res.append(str(bit_sum % 2))
            carry = bit_sum // 2
        return "".join(reversed(res))


# ---------------------------------------------------------
# Problem 3: Factorial Trailing Zeroes (LeetCode 172, Medium)
# Link: https://leetcode.com/problems/factorial-trailing-zeroes/
# ---------------------------------------------------------


class SolutionFactorialTrailingZeroes:
    def trailingZeroes(self, n: int) -> int:
        # Count number of factors of 5
        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Pow(2, 10):", SolutionPowXN().myPow(2, 10))
    print("Add Binary (1010 + 1011):", SolutionAddBinary().addBinary("1010", "1011"))
    print(
        "Trailing zeros in 100!:", SolutionFactorialTrailingZeroes().trailingZeroes(100)
    )
