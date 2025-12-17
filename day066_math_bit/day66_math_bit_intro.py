"""
Day 66: Math / Bit
"""


# -------------------------------
# Example 1: Fast Power (Binary Exponentiation)
# -------------------------------
def example_one(x: float, n: int) -> float:
    # Compute x^n efficiently using exponentiation by squaring
    if n < 0:
        x = 1 / x
        n = -n
    result = 1
    while n:
        if n & 1:  # if last bit of n is 1
            result *= x
        x *= x
        n >>= 1
    return result


print("Output Example 1 (2^10):", example_one(2, 10))
print("Output Example 1 (2^-3):", example_one(2, -3))


# -------------------------------
# Example 2: Binary String Addition
# -------------------------------
def example_two(a: str, b: str) -> str:
    # Add binary strings manually using carry logic
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


print("Output Example 2 ('1010' + '1011'):", example_two("1010", "1011"))


# -------------------------------
# Example 3: Counting Trailing Zeros in Factorial
# -------------------------------
def example_three(n: int) -> int:
    # Count number of factors of 5 in n!
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


print("Output Example 3 (Trailing zeros in 100!):", example_three(100))
