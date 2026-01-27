"""
Day 147: Heap (Priority Queue) - Part 2
Heaps are essential when dynamically maintaining order, medians,
closest elements, or managing constrained greedy choices.
"""

import heapq


# Example 1: Maintain running median using two heaps
def example_one():
    """
    Two-heap technique:
    - Max-heap for lower half
    - Min-heap for upper half
    """
    nums = [5, 2, 10, 4]
    low, high = [], []  # max-heap, min-heap
    medians = []

    for n in nums:
        heapq.heappush(low, -n)
        heapq.heappush(high, -heapq.heappop(low))
        if len(high) > len(low):
            heapq.heappush(low, -heapq.heappop(high))
        medians.append(-low[0])

    return medians


print("Output Example 1:", example_one())


# Example 2: K closest points using max-heap
def example_two():
    """
    Keep heap size at k using negative distances.
    """
    points = [(1, 3), (-2, 2), (5, 8)]
    k = 2
    heap = []

    for x, y in points:
        dist = x * x + y * y
        heapq.heappush(heap, (-dist, x, y))
        if len(heap) > k:
            heapq.heappop(heap)

    return [(x, y) for _, x, y in heap]


print("Output Example 2:", example_two())
