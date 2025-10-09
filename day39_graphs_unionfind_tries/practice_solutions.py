""" 
Day 39: Graphs, Union-Find, Tries - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Course Schedule (LeetCode 207, Medium)
# Link: https://leetcode.com/problems/course-schedule/
# ---------------------------------------------------------

from collections import defaultdict, deque

class SolutionCourseSchedule:
    def canFinish(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        completed = 0

        while q:
            course = q.popleft()
            completed += 1
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return completed == numCourses


# ---------------------------------------------------------
# Problem: Course Schedule II (LeetCode 210, Medium)
# Link: https://leetcode.com/problems/course-schedule-ii/
# ---------------------------------------------------------

class SolutionCourseScheduleII:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while q:
            course = q.popleft()
            order.append(course)
            for nei in graph[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return order if len(order) == numCourses else []


# ---------------------------------------------------------
# Problem: Find Eventual Safe States (LeetCode 802, Medium)
# Link: https://leetcode.com/problems/find-eventual-safe-states/
# ---------------------------------------------------------

class SolutionEventualSafeStates:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        color = [0] * n  # 0=unvisited, 1=visiting, 2=safe

        def dfs(node):
            if color[node] != 0:
                return color[node] == 2
            color[node] = 1
            for nei in graph[node]:
                if color[nei] == 1 or not dfs(nei):
                    return False
            color[node] = 2
            return True

        return [i for i in range(n) if dfs(i)]


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 207 Example:", SolutionCourseSchedule().canFinish(2, [[1, 0]]))
    print("Problem 210 Example:", SolutionCourseScheduleII().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
    print("Problem 802 Example:", SolutionEventualSafeStates().eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]]))
