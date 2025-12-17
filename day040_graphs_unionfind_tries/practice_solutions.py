"""
Day 40: Graphs, Union-Find, Tries - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem 1: Reconstruct Itinerary (LeetCode 332, Hard)
# Link: https://leetcode.com/problems/reconstruct-itinerary/
# ---------------------------------------------------------
from collections import defaultdict, deque

class SolutionItinerary:
    def findItinerary(self, tickets):
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


# ---------------------------------------------------------
# Problem 2: All Nodes Distance K in Binary Tree (LeetCode 863, Medium)
# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# ---------------------------------------------------------
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionNodesDistanceK:
    def distanceK(self, root, target, k):
        from collections import defaultdict, deque

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

        q = deque([(target, 0)])
        visited = {target}
        res = []

        while q:
            node, dist = q.popleft()
            if dist == k:
                res.append(node.val)
            if dist > k:
                break
            for nei in graph[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
        return res


# ---------------------------------------------------------
# Problem 3: Find the City With the Smallest Number of Neighbors (LeetCode 1334, Medium)
# Link: https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
# ---------------------------------------------------------
class SolutionFindCity:
    def findTheCity(self, n, edges, distanceThreshold):
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
            reach = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
            if reach <= minReach:
                minReach = reach
                city = i
        return city


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 332 Example:", SolutionItinerary().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    print("Problem 863 Example:", SolutionNodesDistanceK().distanceK(root, root.left, 2))
    print("Problem 1334 Example:", SolutionFindCity().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
