"""
Day 150: Union-Find (Disjoint Set Union)

Union-Find efficiently manages dynamic connectivity.
Core operations:
- find(x): find representative (with path compression)
- union(x, y): merge two sets (by rank/size)
"""


# Example 1: Basic Union-Find usage
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


def example_one():
    uf = UnionFind(5)
    uf.union(0, 1)
    uf.union(1, 2)
    return uf.find(0) == uf.find(2)


print("Output Example 1:", example_one())


# Example 2: Union-Find for connected components
def example_two():
    edges = [(0, 1), (2, 3), (3, 4)]
    uf = UnionFind(5)
    for u, v in edges:
        uf.union(u, v)

    components = set(uf.find(i) for i in range(5))
    return len(components)


print("Output Example 2:", example_two())
