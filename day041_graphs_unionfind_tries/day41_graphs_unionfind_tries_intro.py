"""
Day 41: Graphs, Union-Find, Tries
"""

# -------------------------------
# Example 1: Longest Consecutive Sequence (HashSet approach)
# -------------------------------
def example_one():
    nums = [100, 4, 200, 1, 3, 2]
    num_set = set(nums)
    longest = 0
    for n in num_set:
        if n - 1 not in num_set:   # Start of a new sequence
            length = 1
            while n + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest

print("Output Example 1 (Longest Consecutive Sequence):", example_one())


# -------------------------------
# Example 2: Graph Valid Tree (Union-Find)
# -------------------------------
def example_two():
    n = 5
    edges = [[0,1],[0,2],[0,3],[1,4]]
    parent = [i for i in range(n)]
    rank = [1]*n

    def find(x):
        while x != parent[x]:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX == rootY:
            return False
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True

    for x, y in edges:
        if not union(x, y):
            return False
    return len(edges) == n - 1

print("Output Example 2 (Graph Valid Tree):", example_two())
