""" Day 87: Graphs – Pathfinding / Traversal / MST
Exploring graph search strategies, weighted pathfinding, and minimum spanning tree concepts.
"""

# Example 1: Dijkstra’s Algorithm (Shortest Path)
def example_one():
    import heapq

    graph = {
        0: [(1, 2), (2, 4)],
        1: [(2, 1)],
        2: [(3, 3)],
        3: []
    }

    dist = {node: float("inf") for node in graph}
    dist[0] = 0

    pq = [(0, 0)]  # (cost, node)

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for nei, w in graph[node]:
            if dist[nei] > cost + w:
                dist[nei] = cost + w
                heapq.heappush(pq, (dist[nei], nei))

    return f"Shortest distance from 0 to 3: {dist[3]}"


print("Output Example 1:", example_one())


# Example 2: Kruskal's MST
def example_two():
    edges = [
        (1, 0, 1),
        (4, 0, 2),
        (2, 1, 2),
        (3, 2, 3),
    ]  # (weight, u, v)

    parent = {i: i for i in range(4)}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parent[pb] = pa

    edges.sort()  # sort by weight
    mst = 0

    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst += w

    return f"MST Weight: {mst}"


print("Output Example 2:", example_two())
