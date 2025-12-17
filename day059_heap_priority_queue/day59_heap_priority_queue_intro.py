"""
Day 59: Heaps / Priority Queues
Understanding min-heaps and max-heaps to efficiently get smallest/largest elements.
"""

import heapq


# Example 1: Find k largest elements
def example_one():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    # heapq.nlargest gives k largest values efficiently using a heap
    return heapq.nlargest(k, nums)


print("Output Example 1:", example_one())


# Example 2: Merge multiple sorted lists (like k sorted arrays)
def example_two():
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    heap = []
    # Push first element of each list
    for i, l in enumerate(lists):
        heapq.heappush(heap, (l[0], i, 0))

    result = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        if element_idx + 1 < len(lists[list_idx]):
            heapq.heappush(
                heap, (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            )
    return result


print("Output Example 2:", example_two())
