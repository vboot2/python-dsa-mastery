"""
Day 75: Intervals / Greedy
"""

# -----------------------------------------------
# Example 1: Interval Greedy (minimum arrows idea)
# -----------------------------------------------

def example_one(intervals):
    """
    Greedy: always shoot an arrow at the smallest ending point of intervals.
    Equivalent to interval scheduling with end-based sorting.
    """
    intervals.sort(key=lambda x: x[1])
    arrows = 1
    end = intervals[0][1]

    for s, e in intervals[1:]:
        if s > end:
            arrows += 1
            end = e
    return arrows

print("Output Example 1:", example_one([[10,16],[2,8],[1,6],[7,12]]))  # Expected: 2


# -----------------------------------------------
# Example 2: Difference Array (range increments)
# -----------------------------------------------

def example_two(n, bookings):
    """
    Difference array:
    - Add value at start index
    - Subtract at end+1 index
    Prefix sum → final array
    """
    diff = [0] * (n + 1)

    for first, last, seats in bookings:
        diff[first - 1] += seats
        diff[last] -= seats

    result = []
    running = 0
    for i in range(n):
        running += diff[i]
        result.append(running)

    return result

print("Output Example 2:", example_two(5, [[1,2,10],[2,3,20],[2,5,25]]))
# Expected: [10,55,45,25,25]
