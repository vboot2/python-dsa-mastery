"""
Day 85: Graphs - Weighted / Traversal - LeetCode Problem Solutions
"""

import heapq

# ---------------------------------------------------------
# Problem 1: 743 – Network Delay Time (Medium)
# Link: https://leetcode.com/problems/network-delay-time/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, times, n, k):
        graph = {i: [] for i in range(1, n+1)}
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {i: float('inf') for i in range(1, n+1)}
        dist[k] = 0
        pq = [(0, k)]

        while pq:
            time, node = heapq.heappop(pq)
            if time > dist[node]:
                continue
            for nei, w in graph[node]:
                new_time = time + w
                if new_time < dist[nei]:
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))

        ans = max(dist.values())
        return ans if ans < float('inf') else -1


# ---------------------------------------------------------
# Problem 2: 787 – Cheapest Flights Within K Stops (Medium)
# Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, n, flights, src, dst, K):
        # Bellman-Ford variant: limit relaxation to K+1 layers
        costs = [float('inf')] * n
        costs[src] = 0

        for _ in range(K+1):
            new = costs[:]
            for u, v, w in flights:
                if costs[u] + w < new[v]:
                    new[v] = costs[u] + w
            costs = new

        return -1 if costs[dst] == float('inf') else costs[dst]


# ---------------------------------------------------------
# Problem 3: 841 – Keys and Rooms (Medium)
# Link: https://leetcode.com/problems/keys-and-rooms/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, rooms):
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == len(rooms)


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Network Delay Time:",
          SolutionProblemOne().solve(
              times=[[2,1,1],[2,3,1],[3,4,1]],
              n=4, k=2))

    print("Cheapest Flights:",
          SolutionProblemTwo().solve(
              4,
              [[0,1,100],[1,2,100],[0,2,500]],
              0, 2, 1))

    print("Keys and Rooms:",
          SolutionProblemThree().solve(
              [[1],[2],[3],[]]))
