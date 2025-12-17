"""
Day 28: Two Pointers, Greedy, Prefix Sum

- Interval List Intersections → two pointers across two sorted interval lists
- Remove Covered Intervals → greedy + sorting by start/end
"""

# -------------------------------
# Example 1: Interval List Intersections
# -------------------------------
def interval_intersection(A, B):
    """
    Use two pointers to walk through both interval lists
    Compare overlapping regions and collect intersections
    """
    i, j = 0, 0
    res = []

    while i < len(A) and j < len(B):
        # Find overlap between A[i] and B[j]
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])

        if start <= end:
            res.append([start, end])

        # Move the pointer with smaller endpoint
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return res


print("Interval Intersections Example:",
      interval_intersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))


# -------------------------------
# Example 2: Remove Covered Intervals
# -------------------------------
def remove_covered_intervals(intervals):
    """
    Greedy approach:
    - Sort intervals by start ascending, end descending
    - Count intervals that are not covered by a previous one
    """
    intervals.sort(key=lambda x: (x[0], -x[1]))
    count = 0
    prev_end = 0

    for _, end in intervals:
        if end > prev_end:
            count += 1
            prev_end = end

    return count


print("Remaining Intervals after removing covered:",
      remove_covered_intervals([[1,4],[3,6],[2,8]]))
