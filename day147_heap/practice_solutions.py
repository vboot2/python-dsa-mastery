"""
Day 147: Heap (Priority Queue) - LeetCode Problem Solutions
"""

import heapq
from collections import Counter, defaultdict
from typing import List, Tuple


# ---------------------------------------------------------
# Problem: Sort Characters By Frequency (LeetCode 451, Medium)
# Link: https://leetcode.com/problems/sort-characters-by-frequency/
# ---------------------------------------------------------
class Solution451:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        res = []
        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch * (-freq))

        return "".join(res)


# ---------------------------------------------------------
# Problem: Find K Closest Elements (LeetCode 658, Medium)
# Link: https://leetcode.com/problems/find-k-closest-elements/
# ---------------------------------------------------------
class Solution658:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for num in arr:
            heapq.heappush(heap, (-abs(num - x), -num))
            if len(heap) > k:
                heapq.heappop(heap)

        return sorted(-num for _, num in heap)


# ---------------------------------------------------------
# Problem: Top K Frequent Words (LeetCode 692, Medium)
# Link: https://leetcode.com/problems/top-k-frequent-words/
# ---------------------------------------------------------
class Solution692:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]


# ---------------------------------------------------------
# Problem: Reorganize String (LeetCode 767, Medium)
# Link: https://leetcode.com/problems/reorganize-string/
# ---------------------------------------------------------
class Solution767:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(heap)

        prev = (0, "")
        res = []

        while heap:
            freq, ch = heapq.heappop(heap)
            res.append(ch)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (freq + 1, ch)

        return "".join(res) if len(res) == len(s) else ""


# ---------------------------------------------------------
# Problem: K-th Smallest Prime Fraction (LeetCode 786, Medium)
# Link: https://leetcode.com/problems/k-th-smallest-prime-fraction/
# ---------------------------------------------------------
class Solution786:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        n = len(arr)

        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(heap)
            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]


# ---------------------------------------------------------
# Problem: Exam Room (LeetCode 855, Medium)
# Link: https://leetcode.com/problems/exam-room/
# ---------------------------------------------------------
class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        init_dist = self._dist(0, n - 1)
        self.heap: List[Tuple[int, int, int]] = [(-init_dist, 0, n - 1)]
        self.start_map = {0: self.heap[0]}
        self.end_map = {n - 1: self.heap[0]}

    def _dist(self, l: int, r: int) -> int:
        if l == 0 or r == self.n - 1:
            return r - l
        return (r - l) // 2

    def _push(self, l: int, r: int) -> None:
        if l > r:
            return
        d = self._dist(l, r)
        entry = (-d, l, r)
        heapq.heappush(self.heap, entry)
        self.start_map[l] = entry
        self.end_map[r] = entry

    def _pop_valid(self) -> Tuple[int, int, int]:
        while self.heap:
            ndist, l, r = heapq.heappop(self.heap)
            if self.start_map.get(l) == (ndist, l, r) and self.end_map.get(r) == (
                ndist,
                l,
                r,
            ):
                del self.start_map[l]
                del self.end_map[r]
                return ndist, l, r
        raise RuntimeError("Heap exhausted – inconsistent state")

    def seat(self) -> int:
        ndist, l, r = self._pop_valid()

        if l == 0:
            seat = 0
        elif r == self.n - 1:
            seat = self.n - 1
        else:
            seat = (l + r) // 2

        if seat > l:
            self._push(l, seat - 1)
        if seat < r:
            self._push(seat + 1, r)

        return seat

    def leave(self, p: int) -> None:
        left_entry = self.end_map.get(p - 1)
        right_entry = self.start_map.get(p + 1)

        new_l = p
        new_r = p

        if left_entry:
            _, l, _ = left_entry
            del self.start_map[l]
            del self.end_map[p - 1]
            new_l = l

        if right_entry:
            _, _, r = right_entry
            del self.start_map[p + 1]
            del self.end_map[r]
            new_r = r

        self._push(new_l, new_r)


# ---------------------------------------------------------
# Problem: Sort an Array (LeetCode 912, Medium)
# Link: https://leetcode.com/problems/sort-an-array/
# ---------------------------------------------------------
class Solution912:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        return [heapq.heappop(nums) for _ in range(len(nums))]


# ---------------------------------------------------------
# Problem: K Closest Points to Origin (LeetCode 973, Medium)
# Link: https://leetcode.com/problems/k-closest-points-to-origin/
# ---------------------------------------------------------
class Solution973:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points:
            heapq.heappush(heap, (-(x * x + y * y), x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]


# ---------------------------------------------------------
# Problem: Distant Barcodes (LeetCode 1054, Medium)
# Link: https://leetcode.com/problems/distant-barcodes/
# ---------------------------------------------------------
class Solution1054:
    def rearrangeBarcodes(self, barcodes) -> List[int]:
        count = Counter(barcodes)
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        prev = (0, None)
        res = []

        while heap:
            freq, num = heapq.heappop(heap)
            res.append(num)
            if prev[0] < 0:
                heapq.heappush(heap, prev)
            prev = (freq + 1, num)

        return res


# ---------------------------------------------------------
# Problem: Car Pooling (LeetCode 1094, Medium)
# Link: https://leetcode.com/problems/car-pooling/
# ---------------------------------------------------------
class Solution1094:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        heap = []
        used = 0

        for num, start, end in trips:
            while heap and heap[0][0] <= start:
                used -= heapq.heappop(heap)[1]
            used += num
            if used > capacity:
                return False
            heapq.heappush(heap, (end, num))

        return True


# ---------------------------------------------------------
# Problem: Trapping Rain Water II (LeetCode 407, Hard)
# Link: https://leetcode.com/problems/trapping-rain-water-ii/
# ---------------------------------------------------------
class Solution407:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap:
            return 0

        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in [0, n - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m - 1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True

        water = 0
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            h, r, c = heapq.heappop(heap)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, h - heightMap[nr][nc])
                    heapq.heappush(heap, (max(h, heightMap[nr][nc]), nr, nc))

        return water


# ---------------------------------------------------------
# Problem: Sliding Window Median (LeetCode 480, Hard)
# Link: https://leetcode.com/problems/sliding-window-median/
# ---------------------------------------------------------
class Solution480:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        low = []
        high = []
        delayed = defaultdict(int)
        lowSize = highSize = 0

        def prune(heap):
            while heap:
                val = -heap[0] if heap is low else heap[0]
                if delayed[val]:
                    heapq.heappop(heap)
                    delayed[val] -= 1
                    if delayed[val] == 0:
                        del delayed[val]
                else:
                    break

        def balance():
            nonlocal lowSize, highSize
            if lowSize > highSize + 1:
                val = -heapq.heappop(low)
                lowSize -= 1
                heapq.heappush(high, val)
                highSize += 1
                prune(low)
            elif lowSize < highSize:
                val = heapq.heappop(high)
                highSize -= 1
                heapq.heappush(low, -val)
                lowSize += 1
                prune(high)

        def add(num: int):
            nonlocal lowSize, highSize
            if not low or num <= -low[0]:
                heapq.heappush(low, -num)
                lowSize += 1
            else:
                heapq.heappush(high, num)
                highSize += 1
            balance()

        def remove(num: int):
            nonlocal lowSize, highSize
            delayed[num] += 1
            if low and num <= -low[0]:
                lowSize -= 1
                if num == -low[0]:
                    prune(low)
            else:
                highSize -= 1
                if high and num == high[0]:
                    prune(high)
            balance()

        def get_median() -> float:
            if k % 2:
                return float(-low[0])
            else:
                return (-low[0] + high[0]) / 2.0

        for i in range(k):
            add(nums[i])
        ans = [get_median()]

        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            ans.append(get_median())

        return ans
