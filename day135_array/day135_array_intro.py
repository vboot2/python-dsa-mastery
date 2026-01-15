"""Day 135: Array
Array based counting, prefix usage, binary search variants,
interval handling, and stock DP problems.
"""


# Example 1: Count primes using Sieve of Eratosthenes
def example_one():
    """
    Mark non-prime numbers efficiently.
    Time Complexity: O(n log log n)
    """
    n = 20
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)


print("Output Example 1:", example_one())


# Example 2: H-Index calculation using sorting
def example_two():
    """
    Sort citations and find maximum h such that
    citations[h] >= h
    """
    citations = [3, 0, 6, 1, 5]
    citations.sort(reverse=True)

    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1

    return h


print("Output Example 2:", example_two())
