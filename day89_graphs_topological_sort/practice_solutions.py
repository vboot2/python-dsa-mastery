""" Day 89: Graphs - Topological Sort - LeetCode Problem Solutions """

from collections import defaultdict, deque

# ---------------------------------------------------------
# Problem: Loud and Rich (LeetCode 851, Medium)
# Link: https://leetcode.com/problems/loud-and-rich/
# ---------------------------------------------------------
class SolutionProblemOne:
    def solve(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        indegree = [0] * n

        # richer[x] = [u, v] meaning u is richer than v → edge u -> v
        for u, v in richer:
            graph[u].append(v)
            indegree[v] += 1

        ans = list(range(n))  # default: each person is quietest for themselves
        q = deque([i for i in range(n) if indegree[i] == 0])

        while q:
            node = q.popleft()
            for nei in graph[node]:
                # propagate quietest known person
                if quiet[ans[node]] < quiet[ans[nei]]:
                    ans[nei] = ans[node]
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return ans


# ---------------------------------------------------------
# Problem: Cat and Mouse (LeetCode 913, Hard)
# Link: https://leetcode.com/problems/cat-and-mouse/
# ---------------------------------------------------------
class SolutionProblemTwo:
    def solve(self, graph):
        # Classic game theory + BFS on states (mouse, cat, turn)
        # 0 = draw, 1 = mouse win, 2 = cat win
        n = len(graph)
        DRAW, MOUSE, CAT = 0, 1, 2

        # dp[mouse][cat][turn]
        dp = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]
        degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]

        for m in range(n):
            for c in range(n):
                degree[m][c][0] = len(graph[m])        # mouse moves
                degree[m][c][1] = len([x for x in graph[c] if x != 0])  # cat moves, cannot go to hole

        from collections import deque
        q = deque()

        # Base cases
        for i in range(n):
            for turn in range(2):
                dp[0][i][turn] = MOUSE
                q.append((0, i, turn, MOUSE))
                if i != 0:
                    dp[i][i][turn] = CAT
                    q.append((i, i, turn, CAT))

        def parents(mouse, cat, turn):
            if turn == 0:
                # mouse moves now, so parents are cat moves
                for pc in graph[cat]:
                    if pc != 0:
                        yield mouse, pc, 1
            else:
                for pm in graph[mouse]:
                    yield pm, cat, 0

        while q:
            mouse, cat, turn, result = q.popleft()
            for pm, pc, pt in parents(mouse, cat, turn):
                if dp[pm][pc][pt] != DRAW:
                    continue
                # If parent can force win
                if (pt == 0 and result == MOUSE) or (pt == 1 and result == CAT):
                    dp[pm][pc][pt] = result
                    q.append((pm, pc, pt, result))
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        dp[pm][pc][pt] = MOUSE if pt == 1 else CAT
                        q.append((pm, pc, pt, dp[pm][pc][pt]))

        return dp[1][2][0]  # start: mouse at 1, cat at 2, mouse turn


# ---------------------------------------------------------
# Problem: Sort Items by Groups Respecting Dependencies (LeetCode 1203, Hard)
# Link: https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/
# ---------------------------------------------------------
class SolutionProblemThree:
    def solve(self, n, m, group, beforeItems):
        # Assign unique group IDs to items with no group
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        # Build item graph and group graph
        item_graph = defaultdict(list)
        item_indeg = [0] * n

        group_graph = defaultdict(list)
        group_indeg = [0] * m

        for i in range(n):
            for pre in beforeItems[i]:
                item_graph[pre].append(i)
                item_indeg[i] += 1

                if group[pre] != group[i]:
                    group_graph[group[pre]].append(group[i])
                    group_indeg[group[i]] += 1

        # Topological sort helper
        def topo_sort(graph, indeg, size):
            q = deque([i for i in range(size) if indeg[i] == 0])
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for nei in graph[node]:
                    indeg[nei] -= 1
                    if indeg[nei] == 0:
                        q.append(nei)
            return order if len(order) == size else []

        group_order = topo_sort(group_graph, group_indeg, m)
        if not group_order:
            return []

        item_order = topo_sort(item_graph, item_indeg, n)
        if not item_order:
            return []

        # Reconstruct output based on group order
        buckets = defaultdict(list)
        for item in item_order:
            buckets[group[item]].append(item)

        res = []
        for g in group_order:
            res.extend(buckets[g])

        return res


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem One Example:",
          SolutionProblemOne().solve(
              [[1,0],[2,1],[3,1]], [3,2,5,4]
          ))

    print("Problem Two Example:",
          SolutionProblemTwo().solve(
              [[2,5],[3],[0,4,5],[4],[5],[]]
          ))

    print("Problem Three Example:",
          SolutionProblemThree().solve(
              8, 2,
              [-1,-1,1,0,0,1,0,-1],
              [[],[6],[5],[6],[3,6],[],[],[]]
          ))
