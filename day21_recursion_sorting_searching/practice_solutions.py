"""
Day 21: Recursion, Sorting, Searching - LeetCode Problem Solutions
"""

# ---------------------------------------------------------
# Problem: Reconstruct Itinerary (LeetCode 332, Hard)
# Link: https://leetcode.com/problems/reconstruct-itinerary/
# ---------------------------------------------------------
from collections import defaultdict
import heapq

class SolutionReconstructItinerary:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)

        result = []
        def dfs(node):
            while graph[node]:
                dfs(heapq.heappop(graph[node]))
            result.append(node)

        dfs("JFK")
        return result[::-1]


# ---------------------------------------------------------
# Problem: Restore IP Addresses (LeetCode 93, Medium)
# Link: https://leetcode.com/problems/restore-ip-addresses/
# ---------------------------------------------------------
class SolutionRestoreIP:
    def restoreIpAddresses(self, s: str):
        result = []

        def backtrack(start, path):
            if len(path) == 4 and start == len(s):
                result.append(".".join(path))
                return
            if len(path) >= 4:
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue
                backtrack(start+length, path+[segment])

        backtrack(0, [])
        return result


# ---------------------------------------------------------
# Example usage
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Problem 332:", SolutionReconstructItinerary().findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
    print("Problem 93:", SolutionRestoreIP().restoreIpAddresses("25525511135"))
