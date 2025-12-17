"""
Day 12: Heaps (Priority Queues)

Heaps are specialized tree-based structures 
that allow quick access to the smallest or largest element.
Python provides `heapq`, which is a min-heap by default.
"""

import heapq

# Example 1: Min-heap
nums = [5, 3, 8, 1, 2]
heapq.heapify(nums)
print("Min-heap:", nums)

# Push and pop
heapq.heappush(nums, 0)
print("After push 0:", nums)

print("Popped element:", heapq.heappop(nums))
print("Heap after pop:", nums)

# Example 2: Max-heap using negative values
nums = [5, 3, 8, 1, 2]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)
print("Max-heap (negated):", max_heap)

# Push and pop
heapq.heappush(max_heap, -10)
print("After push 10:", max_heap)

print("Popped max element:", -heapq.heappop(max_heap))
print("Heap after pop:", max_heap)

# Example 3: Get N smallest/largest
nums = [5, 3, 8, 1, 2, 10, 7]
print("3 smallest:", heapq.nsmallest(3, nums))
print("3 largest:", heapq.nlargest(3, nums))
