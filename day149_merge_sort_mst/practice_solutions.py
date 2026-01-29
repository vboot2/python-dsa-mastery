"""
Day 149: Merge Sort & Minimum Spanning Tree - LeetCode Solutions
"""

from typing import List
from bisect import bisect, bisect_left, bisect_right
from collections import defaultdict


# ---------------------------------------------------------
# Problem: Count Subarrays With Majority Element I (LeetCode 3737, Medium)
# Link: https://leetcode.com/problems/count-subarrays-with-majority-element-i/
# ---------------------------------------------------------
class Solution3737:
    def countSubarrays(self, nums: List[int], target: int) -> int:
        prefix = 0
        sorted_prefix = [0]
        res = 0

        for x in nums:
            prefix += 1 if x == target else -1
            idx = bisect.bisect_left(sorted_prefix, prefix)
            res += idx
            bisect.insort(sorted_prefix, prefix)

        return res


# ---------------------------------------------------------
# Problem: Reverse Pairs (LeetCode 493, Hard)
# Link: https://leetcode.com/problems/reverse-pairs/
# ---------------------------------------------------------
class Solution493:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(arr):
            if len(arr) <= 1:
                return arr, 0

            mid = len(arr) // 2
            left, c1 = sort(arr[:mid])
            right, c2 = sort(arr[mid:])
            count = c1 + c2

            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                count += j

            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1

            merged.extend(left[i:])
            merged.extend(right[j:])
            return merged, count

        return sort(nums)[1]


# ---------------------------------------------------------
# Problem: Create Sorted Array through Instructions (LeetCode 1649, Hard)
# Link: https://leetcode.com/problems/create-sorted-array-through-instructions/
# ---------------------------------------------------------
class Solution1649:
    def createSortedArray(self, instructions: List[int]) -> int:
        MOD = 10**9 + 7
        arr = []
        cost = 0

        for x in instructions:
            left = bisect_left(arr, x)
            right = len(arr) - bisect_right(arr, x)
            cost += min(left, right)
            arr.insert(left, x)

        return cost % MOD


# ---------------------------------------------------------
# Problem: Count Good Triplets in an Array (LeetCode 2179, Hard)
# Link: https://leetcode.com/problems/count-good-triplets-in-an-array/
# ---------------------------------------------------------
class Solution2179:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        pos = {v: i for i, v in enumerate(nums2)}
        mapped = [pos[x] for x in nums1]

        left = [0] * len(mapped)
        seen = []

        for i, x in enumerate(mapped):
            left[i] = bisect_left(seen, x)
            seen.insert(left[i], x)

        seen.clear()
        res = 0
        for i in range(len(mapped) - 1, -1, -1):
            x = mapped[i]
            right = len(seen) - bisect_right(seen, x)
            res += left[i] * right
            seen.insert(bisect_left(seen, x), x)

        return res


# ---------------------------------------------------------
# Problem: Number of Pairs Satisfying Inequality (LeetCode 2426, Hard)
# Link: https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
# ---------------------------------------------------------
class Solution2426:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = [a - b for a, b in zip(nums1, nums2)]

        def sort(nums):
            if len(nums) <= 1:
                return nums, 0

            mid = len(nums) // 2
            left, c1 = sort(nums[:mid])
            right, c2 = sort(nums[mid:])
            count = c1 + c2

            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > right[j] + diff:
                    j += 1
                count += len(right) - j

            return sorted(left + right), count

        return sort(arr)[1]


# ---------------------------------------------------------
# Problem: Min Cost to Connect All Points (LeetCode 1584, Medium)
# Link: https://leetcode.com/problems/min-cost-to-connect-all-points/
# ---------------------------------------------------------
class Solution1584:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                edges.append((cost, i, j))

        edges.sort()
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        res = 0
        for cost, u, v in edges:
            pu, pv = find(u), find(v)
            if pu != pv:
                parent[pu] = pv
                res += cost
                n -= 1
                if n == 1:
                    break

        return res


# ---------------------------------------------------------
# Problem: Find Critical and Pseudo-Critical Edges in MST (LeetCode 1489, Hard)
# Link: https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
# ---------------------------------------------------------
class Solution1489:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        indexed = [(w, u, v, i) for i, (u, v, w) in enumerate(edges)]
        indexed.sort()

        def kruskal(skip=-1, force=None):
            parent = list(range(n))

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            cost = 0
            if force:
                w, u, v, _ = force
                parent[find(u)] = find(v)
                cost += w

            for w, u, v, i in indexed:
                if i == skip:
                    continue
                pu, pv = find(u), find(v)
                if pu != pv:
                    parent[pu] = pv
                    cost += w

            root = find(0)
            return cost if all(find(i) == root for i in range(n)) else float("inf")

        base = kruskal()
        critical, pseudo = [], []

        for e in indexed:
            if kruskal(skip=e[3]) > base:
                critical.append(e[3])
            elif kruskal(force=e) == base:
                pseudo.append(e[3])

        return [critical, pseudo]


# ---------------------------------------------------------
# Problem: Maximize Spanning Tree Stability with Upgrades (LeetCode 3600, Hard)
# Link: https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/
# ---------------------------------------------------------
class Solution3600:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def can(mid):
            parent = list(range(n))
            used = 0
            upgrades = 0

            def find(x):
                if parent[x] != x:
                    parent[x] = find(parent[x])
                return parent[x]

            def union(a, b):
                pa, pb = find(a), find(b)
                if pa == pb:
                    return False
                parent[pa] = pb
                return True

            for u, v, s, must in edges:
                if must == 1:
                    if s < mid:
                        return False
                    if not union(u, v):
                        return False
                    used += 1

            optional = []
            for u, v, s, must in edges:
                if must == 0:
                    optional.append((s, u, v))

            optional.sort(reverse=True)

            for s, u, v in optional:
                if used == n - 1:
                    break
                if find(u) == find(v):
                    continue
                if s >= mid:
                    union(u, v)
                    used += 1
                elif s * 2 >= mid and upgrades < k:
                    upgrades += 1
                    union(u, v)
                    used += 1

            return used == n - 1

        lo, hi = 1, max(s * 2 for _, _, s, _ in edges)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans


# ---------------------------------------------------------
# Problem: Count Subarrays With Majority Element II (LeetCode 3739, Hard)
# Link: https://leetcode.com/problems/count-subarrays-with-majority-element-ii/
# ---------------------------------------------------------
class Solution3739:
    def countSubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        if target not in nums:
            return 0

        counts = [0] * (2 * n + 2)
        prevSum = n + 1
        subArrayCounts = 0
        ans = 0
        counts[prevSum] = 1

        for num in nums:
            if num == target:
                prevSum += 1
                subArrayCounts += counts[prevSum - 1]
            else:
                prevSum -= 1
                subArrayCounts -= counts[prevSum]

            counts[prevSum] += 1

            ans += subArrayCounts

        return ans
