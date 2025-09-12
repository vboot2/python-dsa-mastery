"""
Day 12: Heaps Practice Solutions
"""

import heapq
from typing import List, Optional

# ---------------------------------------------------------
# Problem: Kth Largest Element in an Array (LeetCode 215)
# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
# ---------------------------------------------------------
def findKthLargest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


# ---------------------------------------------------------
# Problem: Merge k Sorted Lists (LeetCode 23)
# Link: https://leetcode.com/problems/merge-k-sorted-lists/
# ---------------------------------------------------------
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class mergekSortedLists:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        # Push first node of each list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
