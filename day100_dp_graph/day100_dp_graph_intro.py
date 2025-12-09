"""
Day 100: DP / Graph
Dynamic Programming and Graph traversal often intersect when problems involve
state transitions over nodes or paths, such as path constraints or multi-factor dependencies.
"""

# ---------------------------------------------------------
# Example 1: DP Example - Minimum steps to reach target using allowed multipliers
# ---------------------------------------------------------
def example_one():
    """
    Simulate a DP approach similar to Super Ugly Numbers (LC 313).
    Maintain multiple pointers for prime factors.
    """
    primes = [2, 3, 5]
    n = 10
    ugly = [1]
    i2 = i3 = i5 = 0

    while len(ugly) < n:
        next_val = min(primes[0]*ugly[i2], primes[1]*ugly[i3], primes[2]*ugly[i5])
        ugly.append(next_val)

        if next_val == primes[0]*ugly[i2]:
            i2 += 1
        if next_val == primes[1]*ugly[i3]:
            i3 += 1
        if next_val == primes[2]*ugly[i5]:
            i5 += 1

    return ugly

print("Output Example 1:", example_one())


# ---------------------------------------------------------
# Example 2: Graph BFS Example - Finding the Town Judge
# ---------------------------------------------------------
def example_two():
    """
    Demonstrate graph indegree-outdegree logic like LC 997.
    """
    N = 3
    trust = [[1, 3], [2, 3]]
    indegree = [0] * (N + 1)
    outdegree = [0] * (N + 1)

    for a, b in trust:
        outdegree[a] += 1
        indegree[b] += 1

    for i in range(1, N + 1):
        if indegree[i] == N - 1 and outdegree[i] == 0:
            return i
    return -1

print("Output Example 2:", example_two())
