"""
Day 61: Union-Find - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Satisfiability of Equality Equations (LeetCode 990, Medium)
# Link: https://leetcode.com/problems/satisfiability-of-equality-equations/
# ---------------------------------------------------------


class Solution990:
    def equationsPossible(self, equations):
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        # First, process all equality equations
        for eq in equations:
            if eq[1:3] == "==":
                union(eq[0], eq[3])

        # Then, check inequalities
        for eq in equations:
            if eq[1:3] == "!=" and find(eq[0]) == find(eq[3]):
                return False

        return True


# ---------------------------------------------------------
# Problem: Smallest String With Swaps (LeetCode 1202, Medium)
# Link: https://leetcode.com/problems/smallest-string-with-swaps/
# ---------------------------------------------------------

from collections import defaultdict


class Solution1202:
    def smallestStringWithSwaps(self, s: str, pairs):
        parent = list(range(len(s)))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Union all connected indices
        for a, b in pairs:
            union(a, b)

        groups = defaultdict(list)
        for i in range(len(s)):
            groups[find(i)].append(i)

        # Reconstruct smallest lexicographic string
        res = list(s)
        for indices in groups.values():
            chars = sorted(res[i] for i in indices)
            for i, ch in zip(sorted(indices), chars):
                res[i] = ch
        return "".join(res)


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print(
        "LeetCode 990 Example:",
        Solution990().equationsPossible(["a==b", "b!=c", "c==a"]),
    )
    print(
        "LeetCode 1202 Example:",
        Solution1202().smallestStringWithSwaps("dcab", [[0, 3], [1, 2], [0, 2]]),
    )
