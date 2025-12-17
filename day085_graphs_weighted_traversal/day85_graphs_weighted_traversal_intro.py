"""
Day 85: Graphs - Weighted / Traversal
Graph algorithms involving weighted shortest paths (Dijkstra),
bounded path search (K stops), and traversal of graph connectivity (DFS/BFS).
"""

# ---------------------------------------------------
# Example 1: Dijkstra’s Algorithm (Shortest Path)
# ---------------------------------------------------
import heapq

def example_one():
    """
    Simple graph shortest path using Dijkstra.
    Graph:
        0 -> 1 (1)
        0 -> 2 (4)
        1 -> 2 (2)
        2 -> 3 (1)
    """
    graph = {
        0: [(1, 1), (2, 4)],
        1: [(2, 2)],
        2: [(3, 1)],
        3: []
    }
    dist = {node: float('inf') for node in graph}
    dist[0] = 0
    pq = [(0, 0)]  # (cost, node)

    while pq:
        cost, node = heapq.heappop(pq)
        if cost > dist[node]:
            continue
        for nei, w in graph[node]:
            new_cost = cost + w
            if new_cost < dist[nei]:
                dist[nei] = new_cost
                heapq.heappush(pq, (new_cost, nei))

    return dist[3]  # shortest path from 0 → 3

print("Output Example 1:", example_one())  # Expected: 0→1→2→3 cost = 1+2+1 = 4


# ---------------------------------------------------
# Example 2: DFS Graph Traversal (Visit All Rooms)
# ---------------------------------------------------
def example_two():
    """
    Simple DFS from room 0 to check reachability.
    """
    rooms = [[1], [2], [3], []]
    seen = set()

    def dfs(node):
        if node in seen:
            return
        seen.add(node)
        for nei in rooms[node]:
            dfs(nei)

    dfs(0)
    return len(seen)

print("Output Example 2:", example_two())  # Expected: 4
