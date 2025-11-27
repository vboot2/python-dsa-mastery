""" Day 88: Graphs – Traversal / Topological Sort - LeetCode Problem Solutions """

from heapq import heappush, heappop
from collections import defaultdict, deque

# ---------------------------------------------------------
# Problem: Reachable Nodes In Subdivided Graph (LeetCode 882, Hard)
# Link: https://leetcode.com/problems/reachable-nodes-in-subdivided-graphs/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, edges, maxMoves, n):
        graph = defaultdict(list)

        # Build weighted graph
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        pq = [(0, 0)]  # (cost, node)
        dist = {i: float("inf") for i in range(n)}
        dist[0] = 0

        # Dijkstra
        while pq:
            cost, node = heappop(pq)
            if cost > dist[node]:
                continue
            for nei, w in graph[node]:
                new_cost = cost + w + 1
                if new_cost < dist[nei] and new_cost <= maxMoves:
                    dist[nei] = new_cost
                    heappush(pq, (new_cost, nei))

        # Count reachable original nodes
        ans = sum(1 for d in dist.values() if d <= maxMoves)

        # Count reachable subdivided nodes
        for u, v, w in edges:
            left = max(0, maxMoves - dist[u])
            right = max(0, maxMoves - dist[v])
            ans += min(w, left + right)

        return ans


# ---------------------------------------------------------
# Problem: Critical Connections in a Network (LeetCode 1192, Hard)
# Link: https://leetcode.com/problems/critical-connections-in-a-network/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, n, connections):
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        low = [0] * n
        ids = [-1] * n
        time = 0
        res = []

        def dfs(node, parent):
            nonlocal time
            ids[node] = low[node] = time
            time += 1
            for nei in graph[node]:
                if nei == parent:
                    continue
                if ids[nei] == -1:
                    dfs(nei, node)
                    low[node] = min(low[node], low[nei])
                    if low[nei] > ids[node]:
                        res.append([node, nei])
                else:
                    low[node] = min(low[node], ids[nei])

        dfs(0, -1)
        return res


# ---------------------------------------------------------
# Problem: Course Schedule IV (LeetCode 1462, Medium)
# Link: https://leetcode.com/problems/course-schedule-iv/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, numCourses, prerequisites, queries):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        q = deque(i for i, deg in enumerate(indegree) if deg == 0)
        topo = []

        while q:
            node = q.popleft()
            topo.append(node)
            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    q.append(nxt)

        reach = [[False] * numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            reach[i][i] = True

        for node in reversed(topo):
            for neigh in graph[node]:
                for k in range(numCourses):
                    if reach[neigh][k]:
                        reach[node][k] = True

        return [reach[u][v] for u, v in queries]


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().solve(
              [[0,1,10],[0,2,1],[1,2,2]], 6, 3))

    print("Problem Two Example:",
          SolutionProblemTwo().solve(4, [[0,1],[1,2],[2,0],[1,3]]))

    print("Problem Three Example:",
          SolutionProblemThree().solve(
              3, [[0,1],[1,2]], [[0,2],[2,0],[1,0]]))
