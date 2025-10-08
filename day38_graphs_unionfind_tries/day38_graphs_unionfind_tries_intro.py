""" 
Day 38: Graphs, Union-Find, Tries
Focus: Connected Components, Cycle Detection, and Account Merging
"""

# Example 1: Count Connected Components using DFS
def example_one():
    """
    Count connected components in an undirected graph.
    """
    graph = {
        0: [1],
        1: [0, 2],
        2: [1],
        3: [4],
        4: [3]
    }

    visited = set()
    components = 0

    def dfs(node):
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                dfs(nei)

    for node in graph:
        if node not in visited:
            visited.add(node)
            dfs(node)
            components += 1

    return components  # Expected 2


# Example 2: Union-Find (Disjoint Set) Implementation
def example_two():
    """
    Union-Find with path compression and union by rank.
    """
    parent = [i for i in range(5)]
    rank = [0] * 5

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX, rootY = find(x), find(y)
        if rootX != rootY:
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

    union(0, 1)
    union(1, 2)
    union(3, 4)
    return parent  # Example of disjoint sets


if __name__ == "__main__":
    print("Output Example 1 (Connected Components):", example_one())
    print("Output Example 2 (Union-Find Sets):", example_two())
