""" 
Day 38: Graphs, Union-Find, Tries - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Number of Provinces (LeetCode 547, Medium)
# Link: https://leetcode.com/problems/number-of-provinces/
# ---------------------------------------------------------

class SolutionNumberOfProvinces:
    def findCircleNum(self, isConnected):
        n = len(isConnected)
        visited = set()

        def dfs(node):
            for nei in range(n):
                if isConnected[node][nei] == 1 and nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        provinces = 0
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i)
                provinces += 1
        return provinces


# ---------------------------------------------------------
# Problem: Redundant Connection (LeetCode 684, Medium)
# Link: https://leetcode.com/problems/redundant-connection/
# ---------------------------------------------------------

class SolutionRedundantConnection:
    def findRedundantConnection(self, edges):
        parent = [i for i in range(len(edges) + 1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]


# ---------------------------------------------------------
# Problem: Accounts Merge (LeetCode 721, Medium)
# Link: https://leetcode.com/problems/accounts-merge/
# ---------------------------------------------------------

from collections import defaultdict

class SolutionAccountsMerge:
    def accountsMerge(self, accounts):
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        email_to_name = {}
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name
                parent.setdefault(email, email)
                union(acc[1], email)

        unions = defaultdict(list)
        for email in parent:
            root = find(email)
            unions[root].append(email)

        return [[email_to_name[root]] + sorted(emails) for root, emails in unions.items()]


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 547 Example:", SolutionNumberOfProvinces().findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
    print("Problem 684 Example:", SolutionRedundantConnection().findRedundantConnection([[1,2],[1,3],[2,3]]))
    print("Problem 721 Example:", SolutionAccountsMerge().accountsMerge([
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ]))
