"""
Day 61: Union-Find (Disjoint Set Union - DSU)
"""


# Example 1: Basic Union-Find Implementation
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            # Path compression
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX, rootY = self.find(x), self.find(y)
        if rootX == rootY:
            return False
        # Union by rank
        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
        return True


def example_one():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    return uf.find(0) == uf.find(2)  # True — all connected


print("Output Example 1:", example_one())


# Example 2: Detecting Cycles in an Undirected Graph
def example_two():
    edges = [(0, 1), (1, 2), (2, 3), (1, 3)]  # 1–3 forms a cycle
    uf = UnionFind(4)
    for u, v in edges:
        if not uf.union(u, v):
            return True  # Cycle detected
    return False


print("Output Example 2:", example_two())
