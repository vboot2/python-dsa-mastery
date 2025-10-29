"""
Day 59: Heaps / Priority Queues - LeetCode Problem Solutions
"""

import heapq
from typing import List

# ---------------------------------------------------------
# Problem: Find Median from Data Stream (LeetCode 295, Hard)
# Link: https://leetcode.com/problems/find-median-from-data-stream/
# ---------------------------------------------------------


class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap (invert values)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if self.small and self.large and (-self.small[0]) > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2


# ---------------------------------------------------------
# Problem: Find K Pairs with Smallest Sums (LeetCode 373, Medium)
# Link: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
# ---------------------------------------------------------


class Solution373:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        heap = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        result = []
        while heap and len(result) < k:
            total, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        return result


# ---------------------------------------------------------
# Problem: Kth Smallest Element in a Sorted Matrix (LeetCode 378, Medium)
# Link: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# ---------------------------------------------------------


class Solution378:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        # Push first element of each row
        for r in range(min(n, k)):
            heapq.heappush(min_heap, (matrix[r][0], r, 0))

        # Pop k-1 smallest elements
        count = 0
        while min_heap:
            val, r, c = heapq.heappop(min_heap)
            count += 1
            if count == k:
                return val
            if c + 1 < len(matrix[0]):
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        return -1


# ---------------------------------------------------------
# Example usage (basic tests)
# ---------------------------------------------------------

if __name__ == "__main__":
    # 295: MedianFinder
    mf = MedianFinder()
    for num in [1, 2, 3, 4]:
        mf.addNum(num)
    print("Problem 295 Example (Median):", mf.findMedian())

    # 373: K Smallest Pairs
    print(
        "Problem 373 Example:", Solution373().kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
    )

    # 378: Kth Smallest in Sorted Matrix
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    print("Problem 378 Example:", Solution378().kthSmallest(matrix, 8))
