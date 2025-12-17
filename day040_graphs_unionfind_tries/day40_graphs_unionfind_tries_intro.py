"""
Day 40: Graphs, Union-Find, Tries
Reconstruct Itinerary, All Nodes Distance K, Shortest Path with Threshold
"""

# -------------------------------
# Example 1: Reconstruct Itinerary (DFS + Backtracking)
# -------------------------------
def example_one():
    """
    Find itinerary using Hierholzer’s algorithm (Eulerian path in directed graph).
    """
    from collections import defaultdict

    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    graph = defaultdict(list)

    for src, dst in sorted(tickets, reverse=True):
        graph[src].append(dst)

    route = []

    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        route.append(airport)

    dfs("JFK")
    return route[::-1]

# -------------------------------
# Example 2: All Nodes Distance K in Binary Tree (DFS + BFS)
# -------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def example_two():
    """
    Return all nodes at distance K from the target node.
    """
    from collections import deque, defaultdict

    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    target = root.left  # node 5
    K = 2

    graph = defaultdict(list)

    def buildGraph(node, parent):
        if not node:
            return
        if parent:
            graph[node].append(parent)
            graph[parent].append(node)
        buildGraph(node.left, node)
        buildGraph(node.right, node)

    buildGraph(root, None)

    visited = set()
    q = deque([(target, 0)])
    res = []

    while q:
        node, dist = q.popleft()
        if dist == K:
            res.append(node.val)
        if dist > K:
            break
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei, dist + 1))

    return res  # Expected [7, 4, 1]


# -------------------------------
# Example 3: Shortest Path with Threshold (Floyd-Warshall)
# -------------------------------
def example_three():
    """
    Compute the city with fewest reachable neighbors within threshold distance.
    """
    n = 4
    edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
    threshold = 4
    INF = float('inf')
    dist = [[INF]*n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
    for u,v,w in edges:
        dist[u][v] = dist[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    minReach, city = n, -1
    for i in range(n):
        reach = sum(1 for j in range(n) if i != j and dist[i][j] <= threshold)
        if reach <= minReach:
            minReach = reach
            city = i

    return city  # Expected output: 3


if __name__ == "__main__":
    print("Output Example 1 (Itinerary):", example_one())
    print("Output Example 2 (Nodes Distance K):", example_two())
    print("Output Example 3 (Shortest Path Threshold):", example_three())
