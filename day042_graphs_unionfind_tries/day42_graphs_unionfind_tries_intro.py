"""
Day 42: Graphs, Union-Find, Tries
"""

# -------------------------------
# Example 1: Bipartite Graph Check using BFS
# -------------------------------
def example_one():
    graph = [[1,2,3],[0,2],[0,1,3],[0,2]]  # Example adjacency list
    color = {}

    for node in range(len(graph)):
        if node not in color:
            queue = [node]
            color[node] = 0
            while queue:
                curr = queue.pop(0)
                for nei in graph[curr]:
                    if nei not in color:
                        color[nei] = 1 - color[curr]
                        queue.append(nei)
                    elif color[nei] == color[curr]:
                        return False
    return True

print("Output Example 1 (Is Graph Bipartite):", example_one())


# -------------------------------
# Example 2: Union-Find to Identify Components
# -------------------------------
def example_two():
    n = 5
    edges = [[0,1],[1,2],[3,4]]
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

    for u, v in edges:
        union(u, v)

    components = len({find(i) for i in range(n)})
    return components

print("Output Example 2 (Number of Components):", example_two())
