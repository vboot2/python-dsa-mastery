"""
Day 21: Recursion, Sorting, Searching
"""

# Example 1: Basic recursion with string splitting
def restore_ip_addresses(s):
    result = []

    def backtrack(start, path):
        # If 4 segments are formed and we used all digits
        if len(path) == 4 and start == len(s):
            result.append(".".join(path))
            return

        # If too many segments or not enough digits left
        if len(path) >= 4:
            return

        # Try splitting 1 to 3 digits
        for end in range(start + 1, min(len(s), start + 3) + 1):
            segment = s[start:end]
            # Skip if invalid (leading zero or >255)
            if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                continue
            backtrack(end, path + [segment])

    backtrack(0, [])
    return result

print("Output Example 1:", restore_ip_addresses("25525511135"))


# Example 2: Lexicographically smallest itinerary using DFS
from collections import defaultdict
import heapq

def find_itinerary(tickets):
    graph = defaultdict(list)
    for src, dst in tickets:
        heapq.heappush(graph[src], dst)

    route = []
    def dfs(airport):
        while graph[airport]:
            dfs(heapq.heappop(graph[airport]))
        route.append(airport)

    dfs("JFK")
    return route[::-1]

print("Output Example 2:", find_itinerary(
    [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
))
